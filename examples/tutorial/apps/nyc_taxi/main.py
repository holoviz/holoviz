import holoviews as hv, geoviews as gv, param, dask.dataframe as dd, cartopy.crs as crs
import panel as pn

from colorcet import cm
from holoviews.operation.datashader import rasterize, shade
from holoviews.streams import RangeXY

hv.extension('bokeh', logo=False)

usecols = ['dropoff_x','dropoff_y','pickup_x','pickup_y','dropoff_hour','pickup_hour','passenger_count']
df = dd.read_parquet('../../data/nyc_taxi_wide.parq')[usecols].persist()
opts = dict(width=1000,height=600,xaxis=None,yaxis=None,bgcolor='black',show_grid=False)
cmaps = ['fire','bgy','bgyw','bmy','gray','kbc']


class NYCTaxiExplorer(param.Parameterized):
    alpha      = param.Magnitude(default=0.75, doc="Alpha value for the map opacity")
    cmap       = param.ObjectSelector(cm['fire'], objects={c:cm[c] for c in cmaps})
    hour       = param.Range(default=(0, 24), bounds=(0, 24))
    location   = param.ObjectSelector(default='dropoff', objects=['dropoff', 'pickup'])

    @param.depends('location', 'hour')
    def points(self):
        points = hv.Points(df, kdims=[self.location+'_x', self.location+'_y'], vdims=['dropoff_hour'])
        if self.hour != (0, 24): points = points.select(dropoff_hour=self.hour)
        return points

    @param.depends('alpha')
    def tiles(self):
        return gv.tile_sources.StamenTerrain.options(alpha=self.alpha, **opts)

    def view(self,**kwargs):
        points = hv.DynamicMap(self.points)
        agg = rasterize(points, x_sampling=1, y_sampling=1, width=600, height=400)
        stream = hv.streams.Params(self, ['cmap'])
        tiles = hv.DynamicMap(self.tiles)
        return tiles * shade(agg, streams=[stream])

taxi = NYCTaxiExplorer(name="NYC Taxi Trips")
pn.Row(taxi.param, taxi.view()).servable()
