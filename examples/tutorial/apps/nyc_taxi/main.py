import os
import holoviews as hv, geoviews as gv, param, parambokeh, dask.dataframe as dd, cartopy.crs as crs

from colorcet import cm_n
from holoviews.operation.datashader import datashade
from holoviews.streams import RangeXY

if __name__ == '__main__':
    hv.extension('bokeh', logo=False)
    
    usecols = ['dropoff_x','dropoff_y','pickup_x','pickup_y','dropoff_hour','pickup_hour','passenger_count']
    df = dd.read_parquet(os.path.join(os.path.dirname(__file__),'..','..','..','data','nyc_taxi_wide.parq'))[usecols].persist()
    
    url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}.jpg'
    tiles = gv.WMTS(url,crs=crs.GOOGLE_MERCATOR)
    opts = dict(width=1000,height=600,xaxis=None,yaxis=None,bgcolor='black',show_grid=False)
    max_pass = int(df.passenger_count.max().compute()+1)
    
    class NYCTaxiExplorer(hv.streams.Stream):
        alpha      = param.Magnitude(default=0.75, doc="Alpha value for the map opacity")
        colormap   = param.ObjectSelector(default=cm_n["fire"], objects=cm_n.values())
        hour       = param.Integer(default=None, bounds=(0, 23), doc="All hours by default; drag to select one hour")
        passengers = param.Range(default=(0,max_pass), bounds=(0,max_pass))
        location   = param.ObjectSelector(default='dropoff', objects=['dropoff', 'pickup'])
    
        def make_view(self, x_range, y_range, **kwargs):
            map_tiles = tiles.options(alpha=self.alpha, **opts)
            points = hv.Points(df, [self.location+'_x', self.location+'_y'], self.location+'_hour')
            selection = {self.location+"_hour":self.hour if self.hour else (0,24), "passenger_count":self.passengers}
            taxi_trips = datashade(points.select(**selection), x_sampling=1, y_sampling=1, cmap=self.colormap,
                                   dynamic=False, x_range=x_range, y_range=y_range, width=1000, height=600)
            return map_tiles * taxi_trips
    
    explorer = NYCTaxiExplorer(name="NYC Taxi Trips")
    dmap = hv.DynamicMap(explorer.make_view, streams=[explorer, RangeXY()])
    
    plot = hv.renderer('bokeh').instance(mode='server').get_plot(dmap)
    parambokeh.Widgets(explorer, view_position='right', callback=explorer.event, plots=[plot.state],
                       mode='server')
