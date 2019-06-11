import os
import dask.dataframe as dd
import holoviews as hv
import parambokeh
import param

from colorcet import cm_n, fire

from bokeh.models import Slider, Button
from bokeh.layouts import layout
from bokeh.io import curdoc

from holoviews.operation.datashader import aggregate, shade
from holoviews.element.tiles import EsriImagery


shade.cmap = fire

hv.extension('bokeh')
renderer = hv.renderer('bokeh').instance(mode='server')

# Load data
ddf = dd.read_parquet(os.path.join(os.path.dirname(__file__),'..','..','..','data','nyc_taxi_wide.parq', engine='fastparquet')).persist()
tiles = EsriImagery()

stream = hv.streams.Stream.define('HourSelect', hour=0)()
points = hv.Points(ddf, kdims=['dropoff_x', 'dropoff_y'])
dmap = hv.util.Dynamic(points, operation=lambda obj, hour: obj.select(dropoff_hour=hour).relabel('Hour of Day: %d' % hour),
                       streams=[stream])

# Apply aggregation
aggregated = aggregate(dmap, link_inputs=True, streams=[hv.streams.RangeXY], width=1200, height=600)

# Shade the data
class ColormapPicker(hv.streams.Stream):
    colormap   = param.ObjectSelector(default=cm_n["fire"], objects=cm_n.values())

cmap_picker = ColormapPicker(rename={'colormap': 'cmap'}, name='')
shaded = shade(aggregated, link_inputs=True, streams=[cmap_picker])

# Define PointerX stream, attach to points and declare DynamicMap for cross-section and VLine
pointer = hv.streams.PointerX(x=ddf.dropoff_x.loc[0].compute().iloc[0], source=points)
section = hv.util.Dynamic(aggregated, operation=lambda obj, x: obj.sample(dropoff_x=x),
                          streams=[pointer], link_inputs=False).relabel('')
vline = hv.DynamicMap(lambda x: hv.VLine(x), streams=[pointer])

# Define options
hv.opts("RGB [width=1200 height=600 xaxis=None yaxis=None fontsize={'title': '14pt'}] VLine (color='white' line_width=2)")
hv.opts("Curve [width=150 yaxis=None show_frame=False] (color='black') {+framewise} Layout [shared_axes=False]")

# Combine it all into a complex layout
hvobj = (tiles * shaded * vline) << section

### Pass the HoloViews object to the renderer
plot = renderer.get_plot(hvobj, doc=curdoc())

# Define a slider and button
start, end = 0, 23

def slider_update(attrname, old, new):
    stream.event(hour=new)

slider = Slider(start=start, end=end, value=0, step=1, title="Hour")
slider.on_change('value', slider_update)

def animate_update():
    year = slider.value + 1
    if year > end:
        year = start
    slider.value = year

def animate():
    if button.label == '\u25B6 Play':
        button.label = '\u23F8 Pause'
        curdoc().add_periodic_callback(animate_update, 500)
    else:
        button.label = '\u25B6 Play'
        curdoc().remove_periodic_callback(animate_update)

button = Button(label='\u25B6 Play', width=60)
button.on_click(animate)

widget = parambokeh.Widgets(cmap_picker, mode='raw')

# Combine the bokeh plot on plot.state with the widgets
layout = layout([
    [widget],
    [plot.state],
    [slider, button],
], sizing_mode='fixed')

curdoc().add_root(layout)
