Background: Why HoloViz?
========================

Many of the activities of an engineer, scientist, or analyst require
visualization, but it can be difficult to assemble a set of tools that
cover all of the tasks involved. Initial exploration needs to be in a
flexible, open-ended environment where it is simple to try out and test
hypotheses. Once key aspects of the data have been identified, the
analyst might prepare a specific image or figure to share with
colleagues or a wider audience. Or, they might need to set up an
interactive way to share a set of data that would be unwieldy as a fixed
figure, using interactive controls to let others explore the effects of
certain variables. Eventually, for particularly important data or use
cases, the analyst might get involved in a long-term project to develop
a full-featured web application or dashboard to deploy, allowing
decision makers to interact directly with live data streams to make
operational decisions.

With Python, initial exploration is typically in a
`Jupyter <http://jupyter.org>`__ notebook, using tools like Matplotlib
and Bokeh to develop static or interactive plots. These tools support a
simple syntax for making certain kinds of plots, but showing more
complex relationships in data can quickly turn into a major software
development exercise, making it difficult to achieve understanding
during exploration. Simple apps can be built using ipywidgets to control
these visualizations, but the resulting combinations end up being
tightly coupled to the notebook environment, unable to migrate into a
standalone server context with an application that can be shared more
widely. Bokeh includes widgets that can work in both notebook and server
environments, but these can be difficult to work with for initial
exploration. Bokeh and Matplotlib both also have limitations on how much
data they can handle, in part because Bokeh requires the data to be put
into the web browser's limited memory space.


The HoloViz ecosystem
-------------------

To address all the above issues, we have developed a set of open-source Python
packages to streamline the process of working with small and large datasets
(from a few datapoints to billions or more) in a web browser, whether doing
exploratory analysis, making simple widget-based tools, or building
full-featured dashboards. The main libraries in this ecosystem include:

-  `Panel <http://panel.pyviz.org>`__: Assembling objects from
   many different libraries into a layout or app, whether in a Jupyter
   notebook or in a standalone servable dashboard
-  `Bokeh <http://bokeh.pydata.org>`__: Interactive plotting in web
   browsers, running JavaScript but controlled by Python
-  `hvPlot <http://hvplot.pyviz.org>`__: Quickly return interactive
   Bokeh-based HoloViews or GeoViews objects from Pandas, Xarray,
   or other data structures
-  `HoloViews <http://holoviews.org>`__: Declarative objects for
   instantly visualizable data, building Bokeh plots from convenient
   high-level specifications
-  `GeoViews <http://geo.holoviews.org>`__: Visualizable geographic
   data that that can be mixed and matched with HoloViews objects
-  `Datashader <http://datashader.org>`__: Rasterizing
   huge datasets quickly as fixed-size images
-  `Param <http://param.pyviz.org>`__: Declaring
   user-relevant parameters, making it simple to work with widgets
   inside and outside of a notebook context


Solving problems using HoloViz tools
----------------------------------

Why do we say that HoloViz is an ecosystem, as opposed to an application
or a tool? The answer is that HoloViz consists of a large set of loosely
related, separately maintained components, not some single monolithic
application. In practice, different people will use different HoloViz
tools in different ways to solve different problems.

For instance, if we focus on the needs of a data scientist/analyst who
wants to understand the properties of their data, we can compare that
to the approach suggested for a software developer wanting to build a
highly custom software application:

.. image:: assets/ds_hv_bokeh.png
    :height: 220px

Here both users are using Datashader, but in very different ways.  The
data analyst could use the high-level interface from HoloViews or
hvPlot, implicitly using Datashader when needed for large datasets,
producing interactive Bokeh-based plots. These interactive plots can
then be used in web browsers directly as static HTML, in Jupyter
Notebooks for interactive sessions, or as a standalone separate
dashboard or application. In each case the analyst pulls in some part
of the ecosystem, as needed.

Meanwhile, a dedicated software developer might use some of these same
tools, perhaps by calling Datashader directly to generate bare images,
and then optionally embedding those images into an interactive Bokeh
plot (or perhaps directly into a report or a web page). This example
covers only a few of the available tools, and each user can apply any
of the tools in combination to solve a huge variety of different
problems.


Shortcuts, not dead ends
------------------------

As you can see, the tools are designed to solve the problems of very
different users working on very different tasks, which reflects the
diversity of users and needs for data visualization.  Casual users
will often want a quick way to get something that works well enough,
while a dedicated technical user with specialized needs will want
detailed control over each aspect, which usually means a different and
more low-level tool.  But because many people fall in between these
extremes, and because individual users often travel on a trajectory
from casual user to power user as their needs become more precise, the
tools are also designed to transition easily between each of these
different approaches.

That is, these tools are designed to offer simplified, high-level
interfaces that are easy ways for users to get started, but those easy
ways should truly be starting points, not dead ends.  To illustrate
this point, consider three different types of tools -- low level, high
level, and layered:

.. image:: assets/shortcuts.png
    :height: 300px

A low-level tool is highly configurable, with an expressive but
relatively verbose command language that makes it possible to
precisely control how it works. For HoloViz, Bokeh is a low-level tool,
allowing any plot or app to be built up from basic primitives. An
even lower-level approach would be to write javascript directly. A
high-level tool like hvPlot or like Panel's interact function uses
much less code and a much simpler interface to make a powerful plot or
dashboard, but what do you do if you then need to make some small
changes in the result?

Typical high-level tools will just be dead ends at this point, forcing
you to start over if what they provide isn't what you needed. HoloViz
high-level tools are instead systematically designed as layers on
top of lower-level tools, where you can use the top level for anything
that it provides, while always being able to drop down a level (or
several if necessary!) to get the behavior you need.

Panel's `interact function <https://panel.pyviz.org/user_guide/Introduction.html>`_
provides a clear example of this approach. With one line of Panel code
you can get a fully functional widget-based app.  But if it's not
precisely what you want, you can then inspect what's returned, unpack
it, rearrange and add or delete components, then use the result
instead.  Similarly, hvPlot provides a one-line way to return complex
HoloViews objects, which can then be inspected, pulled apart,
reconfigured, and recomposed if/as needed. And then these HoloViews
objects, in turn, can be used to make a Bokeh figure that again can be
examined, modified, and used in other contexts (if desired!).


Building on the Python scientific ecosystem
-------------------------------------------

Beyond the specific HoloViz tools, all these approaches work with and
often rely upon a wide range of other open-source libraries for their
implementation, including:

-  `Pandas <http://pandas.pydata.org>`__: Convenient computation on
   columnar datasets (used by HoloViews and datashader)
-  `Xarray <http://xarray>`__: Convenient computations on
   multidimensional array datasets (used by HoloViews and Datashader)
-  `Dask <http://dask.pydata.org>`__: Efficient
   out-of-core/distributed computation on massive datasets (used by
   Datashader)
-  `Numba <http://numba.pydata.org>`__: Accelerated machine code for
   inner loops (used by Datashader)
-  `Fastparquet <https://fastparquet.readthedocs.io>`__: Efficient
   storage for columnar data
-  `Cartopy <http://scitools.org.uk/cartopy>`__: Support for
   geographical data (using a wide range of other lower-level libraries)


These and many other tools form the broader ecosystem that supports
HoloViz. The HoloViz tutorials will guide you through the process of
using these tools together to build rich, high-performance, scalable,
flexible, and deployable visualizations, apps, and dashboards, without
having to use JavaScript or other web technologies explicitly, and
without having to rewrite your code to move between each of the
different tasks or phases from exploration to deployment. In each
case, we'll try to draw your attention to libraries and approaches
that help you get the job done, which in turn depend on many other
unseen libraries in the scientific Python ecosystem to do the heavy
lifting.


Demos
-----

To give you an idea what sort of functionality is possible with these
tools, you can check out some of these links first if you wish:

-  `Selection
   stream <http://holoviews.org/reference/apps/bokeh/selection_stream.html>`__
-  `Bounds
   stream <http://holoviews.org/reference/streams/bokeh/BoundsX.html>`__
-  `Mandelbrot <http://holoviews.org/gallery/apps/bokeh/mandelbrot.html>`__
-  `DynamicMap <http://holoviews.org/reference/containers/bokeh/DynamicMap.html>`__
-  `Crossfilter <http://holoviews.org/gallery/apps/bokeh/crossfilter.html>`__
-  `Game of
   Life <http://holoviews.org/gallery/apps/bokeh/game_of_life.html>`__
-  `Dragon
   curve <http://holoviews.org/gallery/demos/bokeh/dragon_curve.html>`__
-  `Datashader NYC Taxi <https://anaconda.org/jbednar/nyc_taxi>`__
-  `Datashader Graphs <https://anaconda.org/jbednar/edge_bundling>`__
-  `Datashader Landsat
   images <http://datashader.org/topics/landsat.html>`__
-  `Datashader OpenSky <https://anaconda.org/jbednar/opensky>`__


Getting started
---------------

First, you should browse through the already-run versions of the HoloViz
`tutorials <tutorial/index.html>`__ to see what they cover and how it all
works. But everything on this website is a Jupyter Notebook that you can
run yourself, once you follow the  `installation <installation>`__
instructions, so the next step is to try it all out and have fun exploring
it!
