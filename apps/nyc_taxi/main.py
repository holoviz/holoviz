import holoviews as hv, geoviews as gv, param, parambokeh, dask.dataframe as dd, cartopy.crs as crs
import panel as pp

from colorcet import cm
from holoviews.operation.datashader import datashade
from holoviews.streams import RangeXY

hv.extension('bokeh', logo=False)

usecols = ['dropoff_x','dropoff_y','pickup_x','pickup_y','dropoff_hour','pickup_hour','passenger_count']
df = dd.read_parquet('../data/nyc_taxi_wide.parq')[usecols].persist()

url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}.jpg'
tiles = gv.WMTS(url,crs=crs.GOOGLE_MERCATOR)
opts = dict(width=1000,height=600,xaxis=None,yaxis=None,bgcolor='black',show_grid=False)
max_pass = int(df.passenger_count.max().compute()+1)

class NYCTaxiExplorer(hv.streams.Stream):
    alpha      = param.Magnitude(default=0.75, doc="Alpha value for the map opacity")
    colormap   = param.ObjectSelector(default='fire', objects=['fire','bgy','bgyw','bmy','gray','kbc'])
    passengers = param.Range(default=(0,max_pass), bounds=(0,max_pass))
    location   = param.ObjectSelector(default='dropoff', objects=['dropoff', 'pickup'])

    @param.depends('alpha','colormap','passengers','location')
    def view(self, **kwargs):
        map_tiles = tiles.options(alpha=self.alpha, **opts)
        points = hv.Points(df, [self.location+'_x', self.location+'_y'])
        taxi_trips = datashade(points.select(passenger_count=self.passengers),
            x_sampling=1, y_sampling=1, cmap=cm[self.colormap], width=1000, height=600)
        return map_tiles * taxi_trips

explorer = NYCTaxiExplorer(name="NYC Taxi Trips")
r = pp.Row(explorer, explorer.view)
r.server_doc()


