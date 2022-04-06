import pathlib
import colorcet as cc
import pandas as pd
import holoviews as hv
import numpy as np
import panel as pn
import xarray as xr

import hvplot.pandas # noqa: API import
import hvplot.xarray # noqa: API import

pn.extension()

from holoviews.streams import Selection1D

df = pd.read_parquet(pathlib.Path(__file__).parent.parent / 'data' / 'earthquakes-projected.parq')
df = df.set_index(df.time)

most_severe = df[df.mag >= 7]

ds = xr.open_dataarray(pathlib.Path(__file__).parent.parent / 'data' / 'raster' / 'gpw_v4_population_density_rev11_2010_2pt5_min.nc')
cleaned_ds = ds.where(ds.values != ds.nodatavals).sel(band=1)
cleaned_ds.name = 'population'

mag_cmap = cc.CET_L4[::-1]

high_mag_points = most_severe.hvplot.points(
    x='longitude', y='latitude', c='mag', hover_cols=['place', 'time'],
    cmap=mag_cmap, tools=['tap'], selection_line_color='black')

rasterized_pop = cleaned_ds.hvplot.image(
    rasterize=True, cmap='kbc', logz=True, clim=(1, np.nan),
    height=500, width=833, xaxis=None, yaxis=None).opts(bgcolor='black')



def earthquakes_around_point(ds, index, degrees_dist=0.5):
    if not index:
        return ds.iloc[[]]
    row = high_mag_points.data.iloc[index[0]]
    half_dist = degrees_dist / 2.0
    df = ds.data
    nearest = df[((df['latitude'] - row.latitude).abs() < half_dist) 
                 & ((df['longitude'] - row.longitude).abs() < half_dist)]
    return hv.Dataset(nearest)

dataset = hv.Dataset(df)
index_stream = Selection1D(source=high_mag_points, index=[-3])

filtered_ds = dataset.apply(earthquakes_around_point, index=index_stream.param.index)

hv.opts.defaults(
    hv.opts.Histogram(toolbar=None),
    hv.opts.Scatter(toolbar=None)
)

def histogram(ds):
    return ds.data.hvplot.hist(y='mag', bin_range=(0, 10), bins=20, color='red', width=400, height=250)

def scatter(ds):
    return ds.data.hvplot.scatter('time', 'mag', color='green', width=400, height=250, padding=0.1)




# We also redefine the VLine
def vline_callback(index):
    if not index:
        return hv.VLine(0)
    row = most_severe.iloc[index[0]]
    return hv.VLine(row.time).opts(line_width=1, color='black')

dist_slider = pn.widgets.FloatSlider(name='Degree Distance', value=0.5, start=0.1, end=2)

filtered_ds = dataset.apply(earthquakes_around_point, index=index_stream.param.index,
                            degrees_dist=dist_slider)

cmaps  = {n: cc.palette[n] for n in ['kbc', 'fire', 'bgy', 'bgyw', 'bmy', 'gray', 'kbc']}

cmap_selector = pn.widgets.Select(name='Colormap', options=cmaps)

rasterized_pop_cmapped = rasterized_pop.apply.opts(cmap=cmap_selector)

def affected_population(index, distance):
    if not index:
        return "No earthquake was selected."
    sel = most_severe.iloc[index[0]]
    lon, lat = sel.longitude, sel.latitude
    lon_dist = (np.cos(np.deg2rad(lat)) * 111.321543) * distance
    lat_dist = 111.321543 * distance
    hdist = distance / 2.
    mean_density = cleaned_ds.sel(x=slice(lon-hdist, lon+hdist), y=slice(lat+hdist, lat-hdist)).mean().item()
    population = (lat_dist * lon_dist) * mean_density
    return 'Approximate population around {place}, where a magnitude {mag} earthquake hit on {date} is {pop:.0f}.'.format(
        pop=population, mag=sel.mag, place=sel.place, date=sel.time)

def bounds(index, value):
    if not index:
        return hv.Bounds((0, 0, 0, 0))
    sel = most_severe.iloc[index[0]]
    hdist = value / 2.
    lon, lat = sel.longitude, sel.latitude 
    return hv.Bounds((lon-hdist, lat-hdist, lon+hdist, lat+hdist))  

dynamic_bounds = hv.DynamicMap(bounds, streams=[index_stream, dist_slider.param.value])
bound_affected_population = pn.bind(affected_population, index=index_stream.param.index, distance=dist_slider)


title = '## Major Earthquakes 2000-2018'
logo = pn.panel('../assets/usgs_logo.png', width=200, align='center')
widgets = pn.WidgetBox(dist_slider, cmap_selector, margin=5)

header = pn.Row(pn.Column(title, pn.panel(bound_affected_population, width=400)),
                pn.layout.Spacer(width=10), logo, pn.layout.HSpacer(), widgets)

dynamic_scatter = filtered_ds.apply(scatter)
dynamic_histogram = filtered_ds.apply(histogram)
temporal_vline = hv.DynamicMap(vline_callback, streams=[index_stream])
rasterized_pop_cmapped = rasterized_pop.apply.opts(cmap=cmap_selector.param.value)
dynamic_bounds = hv.DynamicMap(bounds, streams=[index_stream, dist_slider.param.value])

body = pn.Row(
    rasterized_pop_cmapped * high_mag_points * dynamic_bounds,
    pn.Column(dynamic_scatter * temporal_vline, dynamic_histogram),
)

pn.Column(header, body).servable()
