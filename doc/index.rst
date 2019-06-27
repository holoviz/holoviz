.. It would be nice to use this as a notebook index.ipynb instead, but unfortunately Jupyter doesn't seem to respect the style options required for resizing logos appropriately, even when embedding as HTML, so it's done as raw HTML here in .rst.

.. raw:: html

    <img src="assets/holoviz-logo-stacked.svg" height="150px">
    <h1>High-level tools to simplify visualization in Python.</h1>

    <p>Welcome to HoloViz!  HoloViz is a coordinated effort to make data visualization in Python easier to use, easier to learn, and more powerful.

    <p>Focusing on interactive plotting in web browsers, HoloViz provides:

    <ul>
    <li>High-level tools that make it easier to apply Python plotting libraries to your data.
    <li>A comprehensive <a href="tutorial">tutorial</a> showing how to use the available tools together to do a wide range of different tasks.
    <li>A <a href="https://conda.io">Conda</a> metapackage "holoviz" that makes it simple to install matching versions of libraries that work well together.
    <li>Sample datasets to work with.
    </ul>

    <h2>Core high-level libraries</h2>
    <style> img.pvlogo { margin:8px; display:inline; object-fit:scale-down; max-height:85px } </style>

    <div style="margin:10px">
    <a href="https://panel.pyviz.org"         ><img class="pvlogo" src="assets/panel.png"/></a>
    <a href="https://hvplot.pyviz.org"         ><img class="pvlogo" src="assets/hvplot.png"/></a>
    <a href="https://holoviews.org"            ><img class="pvlogo" src="assets/holoviews.png"/></a>
    <a href="http://geoviews.org"             ><img class="pvlogo" src="assets/geoviews.png"/></a>
    <a href="http://datashader.org"           ><img class="pvlogo" src="assets/datashader.png"/></a>
    <a href="https://param.pyviz.org"          ><img class="pvlogo" src="assets/param.png"/></a>
    <a href="https://colorcet.pyviz.org"       ><img class="pvlogo" src="assets/colorcet.png"/></a>

    </div>

    <p>These HoloViz-maintained packages each make great starting points --
    <a href="https://panel.pyviz.org">Panel</a>  for making apps and dashboards for your plots from any supported plotting library,
    <a href="https://hvplot.pyviz.org">hvPlot</a> to quickly generate interactive plots from your data,
    <a href="https://holoviews.org">HoloViews</a> to help you make all of your data instantly visualizable,
    <a href="http://geoviews.org">GeoViews</a> to extend HoloViews for geographic data,
    <a href="http://datashader.org">Datashader</a> for rendering of even the largest datasets,
    <a href="https://param.pyviz.org">Param</a> to create declarative user-configurable objects, and
    <a href="https://colorcet.pyviz.org">Colorcet</a> for perceptually uniform colormaps.<br><br>


    <h2>Supported viz libraries</h2>
    <p>HoloViz tools provide extensive support for
    <a href="http://bokeh.pydata.org">Bokeh</a>'s interactive plotting and
    <a href="http://matplotlib.org">Matplotlib</a>'s publication-quality output.
    <br>
    <p>Objects from nearly every other plotting library can be used with
    <a href="https://panel.pyviz.org">Panel</a>, including specific support for
    <a href="http://seaborn.pydata.org">seaborn</a>,
    <a href="https://altair-viz.github.io">altair</a>,
    <a href="https://vega.github.io">vega</a>,
    <a href="https://plotnine.readthedocs.io">plotnine</a>,
    <a href="https://graphviz.org">graphviz</a>,
    <a href="https://ggplot2.tidyverse.org">ggplot2</a>,
    plus anything that can generate HTML, PNG, or SVG.  HoloViews also supports
    <a href="https://plot.ly">Plotly</a> for 3D visualizations.<br><br>


    <h2>Supported data/compute libraries</h2>

    <p>HoloViz core tools work with any Python data types (lists, dictionaries, etc.), plus
    <a href="http://pandas.pydata.org">Pandas</a> or
    <a href="http://dask.pydata.org">Dask</a> DataFrames and
    <a href="http://numpy.org">NumPy</a>,
    <a href="http://xarray.pydata.org">Xarray</a>, or
    <a href="http://dask.pydata.org">Dask</a> arrays, including remote data from the
    <a href="https://intake.readthedocs.io">Intake</a> data catalog library. They also use
    <a href="http://dask.pydata.org">Dask</a> and
    <a href="http://numba.pydata.org">Numba</a> to speed up computations along with algorithms and functions from
    <a href="https://bit.ly/2OXxNfN">SciPy</a>.<br><br>


    <h2>Other supported tools</h2>

    HoloViz tools are general purpose, but also support some domain-specific datatypes like graphs from
    <a href="http://networkx.github.io">NetworkX</a> and geographic data from
    <a href="http://geopandas.org">GeoPandas</a> and
    <a href="http://scitools.org.uk/cartopy">Cartopy</a> and
    <a href="https://scitools.org.uk/iris">Iris</a>.<br>
    Panel can be used with
    <a href="https://yt-project.org">yt</a> for volumetric and physics data and
    <a href="https://sympy.org">SymPy</a> or LaTeX for visualizing equations.<br>
    HoloViz tools provide extensive support for
    <a href="http://jupyter.org">Jupyter</a> notebooks, as well as for standalone web servers and exporting as static files.<br><br>

    <h2>Getting started</h2>

The `Background <background.html>`_ page explains the HoloViz approach in more detail, including how these tools fit together.
Or you can just skim the material in the `Tutorial <tutorial/index.html>`_ online, to get an idea what is covered by these tools.
If what you see looks relevant to you, you can then follow the steps outlined in `Installation <installation.html>`_ to get the libraries, tutorial, and sample data on your own system so you can work through the tutorial yourself. You'll then have simple-to-adapt starting points for solving your own visualization problems using Python.


.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 2

   Introduction <self>
   Background <background>
   Installation <installation>
   Talks <talks/index>
   Tutorial <tutorial/index>
   Topics <topics/index>
   Roadmap <Roadmap>
   FAQ
   About <about>
   Community <community>
