HoloViz Roadmap, as of 8/2022
=============================

HoloViz helps coordinate between numerous independent open-source
projects, each with their own developers, priorities, and agendas. In
large part, the future of HoloViz is up to a distributed team of
developers that focus on the areas of greatest current interest and
need, including areas that specifically get current funding.

Currently scheduled priorities include:

1. **Ongoing maintenance, improved documentation and examples**: As
   always, there are various bugs and usability issues reported on the
   issue tracker, and we will address these as time permits.

2. **Better Datashader integration with external plotting libraries
   (HoloViews, Plotly, Matplotlib)**: Datashader provides its own
   "shading" support, turning an array into colors for display, but if
   shading is done by an external plotting program, the plotting
   program can support user-friendly features like hover information,
   legends, and colorbars. There is already extensive support for
   rendering Datashader output in Bokeh, along with some support in
   Matplotlib and Plotly. The core team is gradually further improving
   Bokeh's support, with nearly all of Datashader's shading
   functionality now or soon available interactively in Bokeh, and
   similar support can be added to other libraries by their users or
   contributors.

3. **Support for managing annotations**: Users of a plot or dashboard
   often notice important features of the data on display, but don't
   have a convenient way to capture or communicate that insight. The
   core team is developing annotations as a first-class component
   the HoloViz tools, easily added onto plots and dashboards so that
   users can denote regions of interest in some space (e.g. a time
   range on a timeseries plot), storing, restoring, and displaying
   that information in editable form.

Other things we'd like to see in HoloViz or in packages designed to work
well with HoloViz include:

1. **More extensive documentation about deployment**: HoloViz includes a
   tutorial on `deployment using Bokeh
   server <http://holoviz.org/tutorial/13_Deploying_Bokeh_Apps.html>`__,
   but there are many other ways to set up live Python-backed plots
   and Panel dashboards or apps, including creating a Flask server or
   embedding into Django, along with deploying via Heroku or Google
   Cloud and AWS or via the Anaconda Enterprise platform or on
   `MyBinder <https://mybinder.org>`__. Documenting and testing these
   possibilities takes time and effort, and any contributions or
   examples that will help people get started and decide between the
   alternatives would be very helpful.

2. **Bokeh WebGL support**: Bokeh provides good support for working
   interactively with small datasets using an HTML Canvas (client-side
   interactivity), and when combined with Datashader it can handle
   enormous datasets by pre-rendering them to images in Python
   (server-side). However, in between these two extremes there is a
   range of data sizes that could be addressed well by the client-side
   WebGL technology. Bokeh has long included some WebGL support, but
   improvements in 2021-2022 have made the WebGL support much more
   solid and usable, and updating HoloViews to use that could bring
   big performance improvements for midsize plots.

3. **Improved imaging, simulation, machine learning, and Earth science
   workflows**: Support for working with image and other
   multidimensional data for visualization and machine-learning
   applications, including on HPC systems.

4. **Simpler deployment of large-scale visualizations**: Automatic
   generation of slippy-map tiles for exploration of large datasets
   using standard web servers. Already provided in Datashader, but
   needs additional polishing.

5. **Integrating 3D surface and volume rendering into HoloViz**: HoloViews
   can plot limited quantities of 3D surface or point data using
   `Matplotlib <http://holoviews.org/reference/elements/matplotlib/TriSurface.html>`__
   or
   `Plotly <http://holoviews.org/reference/elements/plotly/TriSurface.html>`__,
   but other tools are needed for larger datasets or for volumetric
   rendering with transparent/semitransparent voxels. Improving 3D
   support could be as simple as providing examples for using existing
   tools like
   `IPyVolume <https://github.com/maartenbreddels/ipyvolume>`__ and
   `Vaex <http://vaex.astro.rug.nl>`__, or by wrapping JavaScript
   libraries like `ThreeJS <https://threejs.org>`__ and
   `CesiumJS <https://cesiumjs.org>`__.  There's a first `prototype
   for a CesiumJS backend now available <http://assets.holoviews.org/demos/HoloViews_CesiumJS.html>`__,
   but lots more work to do to make it practical for real use.

6. **Additional plot types**: HoloViews includes an extensive range of
   plot types (Elements) covering the typical visualizations used across
   many domains. However, there are always more that can be included,
   and some domains are not as well covered as others. Some examples
   that we'd like to include are:

   -  `parallel
      coordinates <https://en.wikipedia.org/wiki/Parallel_coordinates>`__
      and `radar charts <https://en.wikipedia.org/wiki/Radar_chart>`__
      (polar parallel coordinates, or star charts)
   -  `treemaps <https://en.wikipedia.org/wiki/Treemapping>`__
   -  `dendrograms <https://en.wikipedia.org/wiki/Dendrogram>`__ and
      `cladograms <https://en.wikipedia.org/wiki/Cladogram>`__
   -  `radial trees <https://en.wikipedia.org/wiki/Radial_tree>`__
   -  `packed
      bubbles <https://stackoverflow.com/questions/46131572/making-a-non-overlapping-bubble-chart-in-matplotlib-circle-packing>`__
   -  `funnel charts <https://en.wikipedia.org/wiki/Funnel_chart>`__
   -  `donut charts <https://datavizcatalogue.com/methods/donut_chart.html>`__ (which can be abused to make a `pie chart <https://en.wikipedia.org/wiki/Pie_chart>`__ if you really want)

7. **Interactive Matplotlib plotting**: Right now, HoloViews supports
   Matplotlib primarily as static PNG or SVG output. Matplotlib also
   supports interactive web-based plotting via ipympl, and supporting
   such interactivity could help make Matplotlib be a viable
   alternative for more use cases.

8. **Better native GUI support**: Right now, HoloViz focuses exclusively
   on tools that work well in web browsers, because it aims to support
   the entire workflow from initial exploration to delivery of fully
   functional interactive applications to other stakeholders. One
   consequence is that it doesn't currently support the types of
   interactivity provided by Matplotlib when used with its native GUI
   backends like Qt. It should be feasible to make the interactive
   functionality in HoloViews (e.g. streams and DynamicMaps) support
   native GUI apps as well, allowing the same user code to be applied to
   a wider range of use cases.

9. **Altair/Vega/Vega-lite integration**: HoloViews and Bokeh provide
   declarative syntaxes that can be expressed in purely static form, and
   it should be feasible to write a translator between them and other
   declarative libraries like Altair, Vega, and Vega-Lite. Those
   libraries are currently focused primarily on statistical
   visualizations, not covering areas like multidimensional (image-like)
   plotting where HoloViews and Bokeh are also used, but they offer a
   common interchange format that could be helpful for interoperating
   with other tools. Writing an import and export facility that covers
   the bulk of the shared functionality should not be a major
   undertaking and could open up interesting new applications. For now,
   Altair and Vega-lite visualizations can be specified and then used
   directly with Panel, but not with HoloViews.

10. **hvPlot/HoloViews serialization**: HoloViews uses a declarative design that
   can be represented in a purely textual form, without any Python code.
   An initial implementation allows any Param-based objects (including
   HoloViews objects) to be represented in JSON or YAML, but it needs
   some polishing before it can be put into wide use for saving and
   restoring configurations and layouts.

11. **Better integration with ____**: There are a lot of tools in the
   Python and other scientific software ecosystems that could be
   included in HoloViz or made easily usable from it. NetworkX (already
   usable but not fully exploited yet) is just one example of many;
   suggestions welcome!

If any of the functionality above is interesting to you (or you have
ideas of your own!) and can offer help with implementation, please
open an issue on this repository or on the specific subproject
repository involved. And if you are lucky enough to be in a position
to fund our developers to work on it, please contact
``sales@anaconda.com``.
