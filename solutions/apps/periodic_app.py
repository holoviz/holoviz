import holoviews as hv
import geoviews as gv
import dask.dataframe as dd

from holoviews.operation.datashader import datashade, aggregate, shade
from bokeh.models import WMTSTileSource

renderer = hv.renderer('bokeh')

# Load data
usecols = ['tpep_pickup_datetime', 'dropoff_x', 'dropoff_y']
ddf = dd.read_csv('../data/nyc_taxi.csv', parse_dates=['tpep_pickup_datetime'], usecols=usecols)
ddf['hour'] = ddf.tpep_pickup_datetime.dt.hour
ddf = ddf.persist()

# Declare objects
stream = hv.streams.Counter()
points = hv.Points(ddf, kdims=['dropoff_x', 'dropoff_y'])
dmap = hv.DynamicMap(lambda counter: points.select(hour=counter%24).relabel('Hour: %s' % (counter % 24)),
                     streams=[stream])
shaded = datashade(dmap)

hv.opts('RGB [width=800, height=600, xaxis=None, yaxis=None]')

url = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}.jpg'
wmts = gv.WMTS(WMTSTileSource(url=url))

overlay = wmts * shaded

# Create server document
doc = renderer.server_doc(overlay)
dmap.periodic(1)
