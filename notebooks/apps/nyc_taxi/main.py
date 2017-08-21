import holoviews as hv, geoviews as gv, param, parambokeh, dask.dataframe as dd

from colorcet import cm
from bokeh.models import WMTSTileSource
from holoviews.operation.datashader import datashade
from holoviews.streams import RangeXY, PlotSize

hv.extension('bokeh')

df = dd.read_parquet('../../data/nyc_taxi_hours.parq/').persist()
url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}.jpg'
tiles = gv.WMTS(WMTSTileSource(url=url))
tile_options = dict(width=1000,height=525,xaxis=None,yaxis=None,bgcolor='black',show_grid=False)

passenger_counts = (0, int(df.passenger_count.max().compute()+1))

class NYCTaxiExplorer(hv.streams.Stream):
    alpha      = param.Magnitude(default=0.75, doc="Alpha value for the map opacity")
    colormap   = param.ObjectSelector(default=cm["fire"], objects=[cm[k] for k in cm.keys() if not '_' in k])
    plot       = param.ObjectSelector(default="pickup",   objects=["pickup","dropoff"])
    passengers = param.Range(default=passenger_counts, bounds=passenger_counts)
    output     = parambokeh.view.Plot()

    def make_view(self, x_range, y_range, **kwargs):
        map_tiles = tiles(style=dict(alpha=self.alpha), plot=tile_options)
        points = hv.Points(df, kdims=[self.plot+'_x', self.plot+'_y'], vdims=['passenger_count'])
        if self.passengers != passenger_counts: points = points.select(passenger_count=self.passengers)
        taxi_trips = datashade(points, x_sampling=1, y_sampling=1, cmap=self.colormap,
                               dynamic=False, x_range=x_range, y_range=y_range, width=1000, height=525)
        return map_tiles * taxi_trips

selector = NYCTaxiExplorer(name="NYC Taxi Trips")
selector.output = hv.DynamicMap(selector.make_view, streams=[selector, RangeXY(), PlotSize()])

doc = parambokeh.Widgets(selector, view_position='right', callback=selector.event, mode='server')
