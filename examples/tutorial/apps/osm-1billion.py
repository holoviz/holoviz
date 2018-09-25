import os
import holoviews as hv, geoviews as gv, param, parambokeh, dask.dataframe as dd, cartopy.crs as crs

from holoviews.operation.datashader import datashade
from holoviews.streams import RangeXY
from colorcet import cm_n

hv.extension('bokeh', logo=False)

try:
    df = dd.read_parquet(os.path.join(os.path.dirname(__file__),'..','..','data','osm-1billion.snappy.parq')).persist()
except:
    # TODO: can we provide a small version of the above file?
    print("TODO: (pointer to) instructions to download osm-1billion")
    df = None

url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}.jpg'
map_tiles = gv.WMTS(url,crs=crs.GOOGLE_MERCATOR)

opts1 = dict(width=1000, height=600, xaxis=None, yaxis=None, bgcolor='black', show_grid=False)
opts2 = dict(width=1000, height=600, x_sampling=1, y_sampling=1, dynamic=False)

class OSMExplorer(hv.streams.Stream):
    alpha      = param.Magnitude(default=0.75, doc="Map opacity")
    colormap   = param.ObjectSelector(default=cm_n["fire"], objects=cm_n.values())

    def make_view(self, x_range, y_range, **kwargs):
        tiles  = map_tiles.options(alpha=self.alpha, **opts1)
        points = hv.Points(df, ['x','y'])
        return tiles * datashade(points, cmap=self.colormap, x_range=x_range, y_range=y_range, **opts2)

explorer = OSMExplorer(name="Open Street Map GPS")
dmap = hv.DynamicMap(explorer.make_view, streams=[explorer, RangeXY()])

plot = hv.renderer('bokeh').instance(mode='server').get_plot(dmap)
parambokeh.Widgets(explorer, view_position='right', callback=explorer.event, plots=[plot.state], mode='server')
