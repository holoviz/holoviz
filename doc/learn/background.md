# Background: Why HoloViz?

Many of the activities of an engineer, scientist, or analyst require visualization, but it can be difficult to assemble a set of tools that cover all of the tasks involved. Initial exploration needs to be in a flexible, open-ended environment where it is simple to try out and test hypotheses. Once key aspects of the data have been identified, the analyst might prepare a specific image or figure to share with colleagues or a wider audience. Alternatively, they might set up an interactive way to share a set of data that would be unwieldy as a fixed figure, using interactive controls to let others explore the effects of certain variables. For important data or use cases, the analyst might develop a full-featured web application or dashboard to allow decision-makers to interact directly with live data streams.

With Python, initial exploration is typically in a [Jupyter](https://jupyter.org) notebook, using tools like Matplotlib and Bokeh to develop static or interactive plots. These tools support a simple syntax for making certain kinds of plots, but showing more complex relationships in data can quickly turn into a major software development exercise. Various toolkits like Bokeh, Dash, and ipywidgets allow building apps to control and explore visualizations interactively, but building the app itself can become a major software development task. Plotting libraries also have limitations on how much data they can handle, especially if they require that all data be present in the web browser's memory. As a result, it's challenging to find tools that support the full range of cases for data visualization.

## The HoloViz Ecosystem

**holo**: Greek root, meaning *whole*, *entire*.

To address these issues, we developed a set of open-source Python packages to streamline the entire process of working with small and large datasets (from a few datapoints to billions or more) in a web browser. The HoloViz ecosystem builds on existing plotting libraries like [Bokeh](https://bokeh.org), [Matplotlib](https://matplotlib.org), and [Plotly](https://plot.ly) and includes special-purpose tools to solve visualization challenges:

- [Panel](https://panel.holoviz.org): Assembles objects from many libraries into a layout or app, whether in a Jupyter notebook or as a standalone servable dashboard.
- [hvPlot](https://hvplot.holoviz.org): Quickly returns interactive HoloViews, GeoViews, or Panel objects from Pandas, Xarray, or other data structures.
- [HoloViews](https://holoviews.org): Declarative objects for instantly visualizable data, building Bokeh plots from high-level specifications.
- [GeoViews](https://geoviews.org): Visualizable geographic data that can be mixed with HoloViews objects.
- [Datashader](https://datashader.org): Rasterizes huge datasets quickly as fixed-size images.
- [Lumen](https://lumen.holoviz.org): Framework for visual analytics that allows users to build data-driven dashboards from a simple YAML specification.
- [Colorcet](https://colorcet.holoviz.org): Perceptually uniform colormaps and categorical color sets.

The chart below will help you choose suitable **Data libraries** and **HoloViz APIs** for your data type, along with **Plotting** and **Dashboarding libraries**:

![HoloViz Flowchart](../flowcharts/holoviz.mermaid.svg)

This chart shows how we designed HoloViz tools to fit together, but feel free to combine these tools or other Python libraries however you like. For instance, you don't *have* to use GeoPandas or GeoViews for geospatial data or Datashader for large datasets—these are just suggestions.

## Shortcuts, Not Dead Ends

These tools are designed to solve problems for a range of users, from casual to expert. Many users want a quick solution that works well enough, while technical users want detailed control over each aspect. Since users often evolve from casual to advanced users, these tools are designed to transition smoothly between different approaches.

HoloViz high-level tools provide simplified interfaces that make it easy to start, but they are not dead ends. You can drop down a level to get more control if needed. While you can create a widget-based app with just a couple lines of code, you can further customize the result by unpacking and modifying components as needed.

## Building on the Python Scientific Ecosystem

HoloViz works with and often relies on a wide range of open-source libraries, including:

- [Pandas](https://pandas.pydata.org): For working with columnar datasets.
- [Xarray](https://xarray.pydata.org): For multidimensional array datasets.
- [Dask](https://dask.org): For out-of-core/distributed computation on massive datasets.
- [Numba](https://numba.pydata.org): For accelerated machine code.
- [Fastparquet](https://fastparquet.readthedocs.io): For efficient columnar data storage.
- [Cartopy](https://scitools.org.uk/cartopy): For geographical data support.

The HoloViz tutorials will guide you through using these tools to build high-performance, scalable, and deployable visualizations, apps, and dashboards, without needing JavaScript or other web technologies.

## Demos

Explore these demos to see what's possible with HoloViz tools:

- [Selection stream](https://holoviews.org/reference/apps/bokeh/selection_stream.html)
- [Bounds stream](https://holoviews.org/reference/streams/bokeh/BoundsX.html)
- [Mandelbrot](https://holoviews.org/gallery/apps/bokeh/mandelbrot.html)
- [DynamicMap](https://holoviews.org/reference/containers/bokeh/DynamicMap.html)
- [Crossfilter](https://holoviews.org/gallery/apps/bokeh/crossfilter.html)
- [Game of Life](https://holoviews.org/gallery/apps/bokeh/game_of_life.html)
- [Dragon curve](https://holoviews.org/gallery/demos/bokeh/dragon_curve.html)
- [Datashader NYC Taxi](https://examples.pyviz.org/nyc_taxi/nyc_taxi.html)
- [Datashader Graphs](https://anaconda.org/jbednar/edge_bundling)
- [Datashader Landsat images](https://examples.pyviz.org/landsat/landsat.html)
- [Datashader OpenSky](https://examples.pyviz.org/opensky/opensky.html)

## Getting Started

Browse the already-run versions of the HoloViz [tutorials](tutorial/index) to see what they cover. Then run the tutorials yourself and start exploring!
