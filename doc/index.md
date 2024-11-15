# <img src="assets/holoviz-logo-stacked.svg" height="150px" alt="HoloViz Logo">  
High-level tools to simplify visualization in Python

Welcome to HoloViz! HoloViz is a coordinated effort to make browser-based data visualization in Python easier to use, easier to learn, and more powerful.

HoloViz provides:

- High-level tools that make it easier to apply Python plotting libraries to your data.
- A comprehensive [tutorial](learn/tutorial/index) showing how to use the available tools together to do a wide range of different tasks.
- Sample datasets to work with.

## HoloViz-maintained libraries

<style> img.pvlogo { margin:8px; display:inline; object-fit:scale-down; max-height:75px } </style>

<div style="margin:10px">
    <a href="https://panel.holoviz.org"><img class="pvlogo" src="assets/panel.png" alt="Panel Logo"/></a>
    <a href="https://hvplot.holoviz.org"><img class="pvlogo" src="assets/hvplot.png" alt="hvPlot Logo"/></a>
    <a href="https://holoviews.org"><img class="pvlogo" src="assets/holoviews.png" alt="HoloViews Logo"/></a>
    <a href="https://geoviews.org"><img class="pvlogo" src="assets/geoviews.png" alt="GeoViews Logo"/></a>
    <a href="https://datashader.org"><img class="pvlogo" src="assets/datashader.png" alt="Datashader Logo"/></a>
    <a href="https://lumen.holoviz.org"><img class="pvlogo" src="assets/lumen.png" alt="Lumen Logo"/></a>
    <a href="https://param.holoviz.org"><img class="pvlogo" src="assets/param.png" alt="Param Logo"/></a>
    <a href="https://colorcet.holoviz.org"><img class="pvlogo" src="assets/colorcet.png" alt="Colorcet Logo"/></a>
</div>

HoloViz provides a set of Python packages that make visualization easier, more accurate, and more powerful:

- [Panel](https://panel.holoviz.org): for making apps and dashboards for your plots from any supported plotting library.
- [hvPlot](https://hvplot.holoviz.org): to quickly generate interactive plots from your data.
- [HoloViews](https://holoviews.org): to help you make all of your data instantly visualizable.
- [GeoViews](https://geoviews.org): to extend HoloViews for geographic data.
- [Datashader](https://datashader.org): for rendering even the largest datasets.
- [Lumen](https://lumen.holoviz.org): to build data-driven dashboards from a simple YAML specification.
- [Param](https://param.holoviz.org): to create declarative user-configurable objects.
- [Colorcet](https://colorcet.holoviz.org): for perceptually uniform colormaps.

Not sure where to start? Try [hvPlot](https://hvplot.holoviz.org) for quick and easy one-line plots of your Pandas, Xarray, Dask, and other data types. Or check out [Panel](https://panel.holoviz.org) if you already have visualizations you want to turn into apps or shareable dashboards. Or just work your way through the [tutorial](learn/tutorial/index) to see *all* the things you can do!

## Building on the SciPy/PyData ecosystem

HoloViz tools build on the many excellent visualization tools available in the scientific Python ecosystem, allowing you to access their power conveniently and efficiently. The core tools make use of [Bokeh](http://bokeh.pydata.org)'s interactive plotting, [Matplotlib](http://matplotlib.org)'s publication-quality output, and [Plotly](https://plot.ly)'s interactive 3D visualizations. [Panel](https://panel.holoviz.org) lets you combine any of these visualizations with output from nearly any other Python plotting library, including specific support for:
- [seaborn](https://seaborn.pydata.org)
- [altair](https://altair-viz.github.io)
- [vega](https://vega.github.io)
- [plotnine](https://plotnine.readthedocs.io)
- [graphviz](https://graphviz.org)
- [ggplot2](https://ggplot2.tidyverse.org), plus anything that can generate HTML, PNG, or SVG.

HoloViz tools and examples generally work with any Python standard data types (lists, dictionaries, etc.), plus [Pandas](https://pandas.pydata.org) or [Dask](https://dask.pydata.org) DataFrames and [NumPy](https://numpy.org), [Xarray](https://xarray.pydata.org), or [Dask](https://dask.pydata.org) arrays, including remote data from the [Intake](https://intake.readthedocs.io) data catalog library. They also use [Dask](https://dask.pydata.org) and [Numba](https://numba.pydata.org) to speed up computations along with algorithms and functions from [SciPy](https://bit.ly/2OXxNfN), and support both GPUs and CPUs to make use of all your available hardware.

HoloViz tools are designed for general-purpose use, but also support some domain-specific datatypes like graphs from [NetworkX](https://networkx.github.io) and geographic data from [GeoPandas](https://geopandas.org), [Cartopy](https://scitools.org.uk/cartopy), and [Iris](https://scitools.org.uk/iris).

HoloViz tools provide extensive support for [Jupyter](https://jupyter.org) notebooks, as well as for standalone Python-backed web servers and exporting visualizations or apps as images or static HTML files.

## Getting Started

The [Background](learn/background) page explains the HoloViz approach in more detail, including how these tools fit together. Or you can just skim the material in the [Tutorial](learn/tutorial/index) online, to get an idea of what is covered by these tools. If what you see looks relevant to you, you can work through the tutorial on your own system. You'll then have simple-to-adapt starting points for solving your own visualization problems using Python.

```{toctree}
:maxdepth: 2
:hidden:
:titlesonly:

Learn <learn/index>
Examples <https://examples.holoviz.org/>
Community <community>
Contribute <contribute>
Blog <https://blog.holoviz.org/>
About <about/index>