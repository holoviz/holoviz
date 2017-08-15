import dask.dataframe as dd
import holoviews as hv
from holoviews.operation.datashader import datashade

# 1. Instead of using hv.extension, declare that we are using Bokeh and grab the renderer
renderer = hv.renderer('bokeh')

# 2. Load data and datashade it
ddf = dd.read_csv('../data/nyc_taxi.csv', usecols=['dropoff_x', 'dropoff_y']).persist()
points = hv.Points(ddf, kdims=['dropoff_x', 'dropoff_y'])
shaded = datashade(points).opts(plot=dict(width=800, height=600))

# 3. Instead of Jupyter's automatic rich display, render the object as a bokeh document
doc = renderer.server_doc(shaded)
doc.title = 'HoloViews Bokeh App'
