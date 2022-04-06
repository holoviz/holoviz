import pathlib
import pandas as pd
import hvplot.pandas  # noqa
from holoviews.element import tiles

from holoviews import streams

import holoviews as hv
hv.extension("bokeh")

import panel as pn


df = pd.read_parquet(pathlib.Path(__file__).parent.parent / 'data' / 'earthquakes-projected.parq')
df = df.set_index(df.time)

most_severe = df[df.mag >= 7]
high_mag_quakes = most_severe.hvplot.points(x='easting', y='northing', c='mag', 
                                                      title='Earthquakes with magnitude >= 7')
esri = tiles.ESRI().redim(x='easting', y='northing')



selection_stream = streams.Selection1D(source=high_mag_quakes)

hv.opts.defaults(hv.opts.Points(nonselection_alpha=0.4))

def labelled_callback(index):
    if len(index) == 0:
        return  hv.Text(x=0,y=0, text='')
    first_index = index[0] # Pick only the first one if multiple are selected
    row = most_severe.iloc[first_index]
    text = '%d : %s' % (first_index, row.place)
    return hv.Text(x=row.easting, y=row.northing, text=text).opts(color='white')

labeller = hv.DynamicMap(labelled_callback, streams=[selection_stream])

def mark_earthquake(index):
    if len(index) == 0:
        return  hv.Overlay([])
    first_index = index[0] # Pick only the first one if multiple are selected
    row = most_severe.iloc[first_index]
    return (hv.Ellipse(row.easting, row.northing, 1.5e6) *
            hv.Ellipse(row.easting, row.northing, 3e6)).opts(
        hv.opts.Ellipse(color='white', alpha=0.5)
    )

quake_marker = hv.DynamicMap(mark_earthquake, streams=[selection_stream])


def earthquakes_around_point(df, lat, lon, degrees_dist=0.5):
    half_dist = degrees_dist / 2.0
    return df[((df['latitude'] - lat).abs() < half_dist) 
              & ((df['longitude'] - lon).abs() < half_dist)]

def index_to_selection(indices, cache={}):
    if not indices: 
        return most_severe.iloc[[]]
    index = indices[0]   # Pick only the first one if multiple are selected
    if index in cache: return cache[index]
    row = most_severe.iloc[index]
    selected_df = earthquakes_around_point(df, row.latitude, row.longitude)
    cache[index] = selected_df
    return selected_df 


def histogram_callback(index):
    title = 'Distribution of all magnitudes within half a degree of selection'
    selected_df = index_to_selection(index)
    return selected_df.hvplot.hist(y='mag', bin_range=(0,10), bins=20, color='red', title=title)

histogram = hv.DynamicMap(histogram_callback, streams=[selection_stream])

def scatter_callback(index):
    title = 'Temporal distribution of all magnitudes within half a degree of selection '
    selected_df = index_to_selection(index)
    return selected_df.hvplot.scatter('time', 'mag', color='green', title=title)

temporal_distribution = hv.DynamicMap(scatter_callback, streams=[selection_stream])

def vline_callback(index):
    if not index:
        return hv.VLine(0).opts(alpha=0)
    row = most_severe.iloc[index[0]]
    return hv.VLine(row.time).opts(line_width=2, color='black')

temporal_vline = hv.DynamicMap(vline_callback, streams=[selection_stream])

column = pn.Column(((esri * high_mag_quakes.opts(tools=['tap']) * labeller * quake_marker)
 + histogram + temporal_distribution * temporal_vline).cols(1))

column.servable(title='Custom Interactivity Demo')

