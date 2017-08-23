import holoviews as hv, geoviews as gv, param, parambokeh, dask.dataframe as dd

from colorcet import cm
from bokeh.models import WMTSTileSource
from holoviews.operation.datashader import datashade
from holoviews.streams import RangeXY, PlotSize

hv.extension('bokeh')

df = dd.read_parquet('../data/nyc_taxi_hours.parq/').persist()
url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}.jpg'
tiles = gv.WMTS(WMTSTileSource(url=url))
tile_options = dict(width=1000,height=600,xaxis=None,yaxis=None,bgcolor='black',show_grid=False)

class NYCTaxiExplorer(hv.streams.Stream):
    alpha      = param.Magnitude(default=0.75, doc="Alpha value for the map opacity")
    colormap   = param.ObjectSelector(default=cm["fire"], objects=[cm[k] for k in cm.keys() if not '_' in k])
    hour       = param.Range(default=(0, 24), bounds=(0, 24))
    location   = param.ObjectSelector(default='dropoff', objects=['dropoff', 'pickup'])

    def make_view(self, x_range, y_range, **kwargs):
        map_tiles = tiles(style=dict(alpha=self.alpha), plot=tile_options)
        points = hv.Points(df, kdims=[self.location+'_x', self.location+'_y'], vdims=['dropoff_hour'])
        if self.hour != (0, 24): points = points.select(dropoff_hour=self.hour)
        taxi_trips = datashade(points, x_sampling=1, y_sampling=1, cmap=self.colormap,
                               dynamic=False, x_range=x_range, y_range=y_range,
                               width=1000, height=600)
        return map_tiles * taxi_trips

selector = NYCTaxiExplorer(name="NYC Taxi Trips")
dmap = hv.DynamicMap(selector.make_view, streams=[selector, RangeXY()])
plot = hv.renderer('bokeh').instance(mode='server').get_plot(dmap)

parambokeh.Widgets(selector, view_position='right', callback=selector.event,
                   mode='server', plots=[plot.state])
