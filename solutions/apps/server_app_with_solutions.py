import dask.dataframe as dd
import holoviews as hv
import geoviews as gv

from bokeh.models import WMTSTileSource
from holoviews.operation.datashader import datashade

url = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}.jpg'
wmts = WMTSTileSource(url=url)

# 1. Instead of using hv.extension, declare that we are using Bokeh and grab the renderer
renderer = hv.renderer('bokeh')


# 2. Declare points and datashade them
ddf = dd.read_csv('../data/nyc_taxi.csv', usecols=['pickup_x', 'pickup_y']).persist()
shaded = datashade(hv.Points(ddf))

# Set some plot options
app = gv.WMTS(wmts) * shaded.opts(plot=dict(width=800, height=600))

# 3. Instead of Jupyter's automatic rich display, render the object as a bokeh document
doc = renderer.server_doc(app)
doc.title = 'HoloViews Bokeh App'
