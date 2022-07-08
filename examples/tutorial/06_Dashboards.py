import pathlib
import pandas as pd
import panel as pn
import holoviews as hv

pn.extension('tabulator', template='material', sizing_mode='stretch_width')

import hvplot.pandas # noqa

df = pd.read_parquet(pathlib.Path(__file__).parent.parent / 'data' / 'earthquakes-projected.parq')
df = df.set_index('time').tz_convert(None).reset_index()

WEB_MERCATOR_LIMITS = (-20037508.342789244, 20037508.342789244)

subset_df = df[
    (df['northing']  < WEB_MERCATOR_LIMITS[1]) &
    (df['mag']       > 4) &
    (df['time']     >= pd.Timestamp('2017-01-01')) &
    (df['time']     <= pd.Timestamp('2018-01-01'))]

date_subrange = pn.widgets.DateRangeSlider(name='Date', 
                                        start=subset_df.time.iloc[0], 
                                        end=subset_df.time.iloc[-1])
mag_subrange = pn.widgets.FloatSlider(name='Magnitude', start=3, end=9, value=3)

subset_dfi = subset_df.interactive(sizing_mode='stretch_width')
filtered_subrange = subset_dfi[
    (subset_dfi['mag']   > mag_subrange) &
    (subset_dfi['time'] >= date_subrange.param.value_start) &
    (subset_dfi['time'] <= date_subrange.param.value_end)]



pn.state.template.sidebar_width = 250
pn.state.template.title = 'Earthquake Interactive Demo'

ls = hv.link_selections.instance(unselected_alpha=0.02)

# Table is not yet dynamically linked to the linked selection
table = filtered_subrange.pipe(ls.filter, selection_expr=ls.param.selection_expr)[['time', 'place', 'mag', 'depth']].pipe(
    pn.widgets.Tabulator, pagination='remote', page_size=15)

mag_hist = filtered_subrange.hvplot(
    y='mag', kind='hist', responsive=True, min_height=300)

depth_hist = filtered_subrange.hvplot(
    y='depth', kind='hist', responsive=True, min_height=300)

geo = filtered_subrange.hvplot(
    'easting', 'northing', color='mag', kind='points',
    xaxis=None, yaxis=None, responsive=True, min_height=500,
    data_aspect=1, framewise=True, clim=(4, 10), line_color='black'
)

column = pn.Column(
    pn.Row(
        hv.element.tiles.ESRI() * ls(geo.holoviews()),
        table.panel()
    ),
    pn.Row(
        ls(depth_hist.holoviews()),
        ls(mag_hist.holoviews()),
    )
)

filtered_subrange.widgets().servable(area='sidebar')

column.servable(title='Earthquake Interactive Demo')
