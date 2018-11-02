.. It would be nice to use this as a notebook index.ipynb instead, but unfortunately Jupyter doesn't seem to respect the style options required for resizing logos appropriately, even when embedding as HTML, so it's done as raw HTML here in .rst.

.. raw:: html

    <img src="assets/PyViz_logo_wm.png" height="150px" align="right">
    <h1>How to visualize data in Python</h1>

    <p>Welcome to PyViz!  PyViz is a coordinated effort to make data visualization in Python easier to use, easier to learn, and more powerful.

    <p>Focusing on interactive plotting in web browsers, PyViz provides:

    <ul>
    <li>High-level tools that make it easier to apply Python plotting libraries to your data.
    <li>A comprehensive <a href="tutorial/index">tutorial</a> showing how to use the available tools together to do a wide range of different tasks.
    <li>A <a href="https://conda.io">Conda</a> metapackage "pyviz" that makes it simple to install matching versions of libraries that work well together.
    <li>Sample datasets to work with.
    </ul>

    <h1>Core high-level libraries</h1>
    <style> img.pvlogo { margin:8px; display:inline; object-fit:scale-down; max-height:85px } </style>

    <div style="margin:10px">
    <a href="https://panel.pyviz.org"         ><img class="pvlogo" src="assets/panel.png"/></a>
    <a href="http://hvplot.pyviz.org"         ><img class="pvlogo" src="assets/hvplot.png"/></a>
    <a href="http://holoviews.org"            ><img class="pvlogo" src="assets/holoviews.png"/></a>
    <a href="http://geoviews.org"             ><img class="pvlogo" src="assets/geoviews.png"/></a>
    </div>

    <p>These PyViz-maintained packages each make great starting points --
    <a href="https://panel.pyviz.org">Panel</a>  for making apps and dashboards for your plots from any supported plotting library,
    <a href="http://hvplot.pyviz.org">hvPlot</a> to quickly generate interactive plots from your data,
    <a href="http://holoviews.org">HoloViews</a> to help you make all of your data instantly visualizable, and 
    <a href="http://geoviews.org">GeoViews</a>   to extend HoloViews for geographic data.<br><br>


    <h1>Supported viz libraries</h1>
    <div style="margin:10px">
    <a href="http://bokeh.pydata.org"         ><img class="pvlogo" src="assets/bokeh.png"/></a>
    <a href="http://matplotlib.org"           ><img class="pvlogo" src="assets/matplotlib_wm.png"/></a>
    <a href="http://datashader.org"           ><img class="pvlogo" src="assets/datashader.png"/></a>
    </div>
    <p>PyViz tools provide extensive support for
    <a href="http://bokeh.pydata.org">Bokeh</a>'s interactive plotting,
    <a href="http://matplotlib.org">Matplotlib</a>'s publication-quality output, and
    <a href="http://datashader.org">Datashader</a>'s rendering of even the largest datasets.
    <br>
    <div style="margin:10px">
    <a href="https://plot.ly"                 ><img class="pvlogo" src="assets/plotly.png"/></a>
    <a href="https://altair-viz.github.io"    ><img class="pvlogo" src="assets/altair.png" style="max-height:75px"/></a>
    <a href="http://seaborn.pydata.org"       ><img class="pvlogo" src="assets/seaborn.png"/></a>
    <a href="https://plotnine.readthedocs.io" ><img class="pvlogo" src="assets/plotnine.png"/></a>
    <a href="https://graphviz.org"            ><img class="pvlogo" src="assets/graphviz.png"/></a>
    <a href="https://ggplot2.tidyverse.org"   ><img class="pvlogo" src="assets/ggplot2.png"/></a>
    <a href="https://python-pillow.org"       ><img class="pvlogo" src="assets/pillow.png"/></a>
    </div>

    <p>Output from nearly every other plotting library can be used with
    <a href="https://panel.pyviz.org">Panel</a>, including all those listed here plus anything that can generate HTML, PNG, or SVG.
    HoloViews also supports
    <a href="https://plot.ly">Plotly</a> for 3D visualizations.<br><br>


    <h1>Supported data/compute libraries</h1>

    <div style="margin:10px">
    <a href="http://pandas.pydata.org"        ><img class="pvlogo" src="assets/pandas.png" style="max-height:80px"/></a>
    <a href="http://numpy.org"                ><img class="pvlogo" src="assets/numpy.png"  style="max-height:95px"/></a>
    <a href="http://xarray.pydata.org"        ><img class="pvlogo" src="assets/xarray_wm.png"/></a>
    <a href="http://dask.pydata.org"          ><img class="pvlogo" src="assets/dask.png"   style="max-height:80px"/></a>
    <a href="http://numba.pydata.org"         ><img class="pvlogo" src="assets/numba.png"  style="max-height:115px"/></a>
    <a href="https://intake.readthedocs.io"   ><img class="pvlogo" src="assets/intake.png" style="max-height:75px"/></a>
    <a href="https://bit.ly/2OXxNfN"          ><img class="pvlogo" src="assets/scipy.png"/></a>
    </div>

    <p>PyViz core tools work with any Python data types (lists, dictionaries, etc.), plus
    <a href="http://pandas.pydata.org">Pandas</a> or
    <a href="http://dask.pydata.org">Dask</a> DataFrames and
    <a href="http://numpy.org">NumPy</a>,
    <a href="http://xarray.pydata.org">Xarray</a>, or
    <a href="http://dask.pydata.org">Dask</a> arrays, including remote data from the 
    <a href="https://intake.readthedocs.io">Intake</a> data catalog library. They also use
    <a href="http://dask.pydata.org">Dask</a> and
    <a href="http://numba.pydata.org">Numba</a> to speed up computations along with algorithms and functions from
    <a href="https://bit.ly/2OXxNfN">SciPy</a>.<br><br>


    <br><h1>Other supported tools</h1>

    <div style="margin:10px">
    <a href="http://networkx.github.io"       ><img class="pvlogo" src="assets/networkx.png"/></a>
    <a href="http://scitools.org.uk/cartopy"  ><img class="pvlogo" src="assets/cartopy.png" style="max-height:70px"/></a>
    <a href="https://scitools.org.uk/iris"    ><img class="pvlogo" src="assets/iris.png"/></a>
    <a href="https://yt-project.org"          ><img class="pvlogo" src="assets/yt.png" style="max-height:70px" /></a>
    <a href="https://sympy.org"               ><img class="pvlogo" src="assets/sympy.png"/></a>
    <a href="http://param.pyviz.org"          ><img class="pvlogo" src="assets/param.png"/></a>
    <a href="http://jupyter.org"              ><img class="pvlogo" src="assets/jupyter.png"/></a>
    </div>
    
    <p>PyViz tools are general purpose, but also support some domain-specific datatypes like graphs from
    <a href="http://networkx.github.io">NetworkX</a> and geographic data from
    <a href="http://scitools.org.uk/cartopy">Cartopy</a> and
    <a href="https://scitools.org.uk/iris">Iris</a>.<br>
    Panel can be used with
    <a href="https://yt-project.org">yt</a> for volumetric and physics data and
    <a href="https://sympy.org">SymPy</a> or LaTeX for visualizing equations.<br>
    PyViz tools both use and support declarative
    <a href="http://param.pyviz.org">Param</a> objects, and provide extensive support both for 
    <a href="http://jupyter.org">Jupyter</a> notebooks as well as standalone servers and exporting to static files.<br><br>
    
    <h1>Getting started</h1>

The `Background <background.html>`_ page explains the PyViz approach in more detail, including how these tools fit together.
Or you can just skim the material in the `Tutorial <tutorial/index.html>`_ online, to get an idea what is covered by these tools.
If what you see looks relevant to you, you can then follow the steps outlined in `Installation <installation.html>`_ to get the libraries, tutorial, and sample data on your own system so you can work through the tutorial yourself. You'll then have simple-to-adapt starting points for solving your own visualization problems using Python.

.. No logo available yet for http://geopandas.org, http://colorcet.pyviz.org, https://vega.github.io, or https://vega.github.io/vega-lite


.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 2

   Introduction <self>
   Background <background>
   Installation <installation>
   Tutorial <tutorial/index>
   Topics <topics/index>
   Roadmap <Roadmap>
   FAQ
   About <about>
