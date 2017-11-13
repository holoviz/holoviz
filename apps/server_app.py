import dask.dataframe as dd
import holoviews as hv
from holoviews.operation.datashader import datashade

hv.extension('bokeh')

# 1. Load data and Datashade it
ddf = dd.read_parquet('../data/nyc_taxi_wide.parq')[['dropoff_x', 'dropoff_y']].persist()
points = hv.Points(ddf, kdims=['dropoff_x', 'dropoff_y'])
shaded = datashade(points).opts(plot=dict(width=800, height=600))

# 2. Instead of Jupyter's automatic rich display, render the object as a bokeh document
doc = hv.renderer('bokeh').server_doc(shaded)
doc.title = 'HoloViews Bokeh App'
