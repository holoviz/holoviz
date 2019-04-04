PyViz Roadmap, as of 10/2018
============================

PyViz helps coordinate between numerous independent open-source
projects, each with their own developers, priorities, and agendas. In
large part, the future of PyViz is up to a distributed team of
developers that focus on the areas of greatest current interest and
need, including areas that specifically get current funding.

Immediate, already funded priorities for 2018 include:

1. **Ongoing maintenance, improved documentation and examples**: As
   always, there are various bugs and usability issues reported on the
   issue tracker, and we will address these as time permits.

2. **Better dashboard/app support**: Making it simpler to make powerful
   dashboards starting from code that works well in a Jupyter notebook,
   including as a simple report, a notebook-backed arbitrary screen
   layout, and sharing components between notebooks and complex deployed
   apps.

3. **Improved imaging, simulation, machine learning, and Earth science
   workflows**: Support for working with image and other
   multidimensional data for visualization and machine-learning
   applications, including on HPC systems.

4. **Improvements to Bokeh/HoloViews drawing tools**:

   - Better support for collecting annotations
   - other usability improvements

5. **Simpler deployment of large-scale visualizations**: Automatic
   generation of slippy-map tiles for exploration of large datasets
   using standard web servers. Already provided in Datashader, but
   needs additional polishing.

6. **Better Datashader integration with external plotting libraries
   (Bokeh, HoloViews, Matplotlib)**: Datashader needs to provide
   functions for supporting hover information, legends, colorbars, and
   interactivity, which each plotting library can then use.

7. **Support for maintaining Python-based projects**: As maintainers of
   a wide range of Python projects, we are working to minimize the cost
   of maintaining each one, by sharing code for tracking versions,
   making releases, providing example scripts, managing datasets,
   documenting examples, testing examples (including notebooks), and
   building websites. Projects addressing each of these areas are being
   added to the `PyViz Github organization <//github.com/pyviz>`__
   and will be documented in the main PyViz site as they become mature.

   
Other things we'd like to see in PyViz or in packages designed to work
well with PyViz include:


1. **Bokeh WebGL support**: Bokeh provides good support for working
   interactively with small datasets using an HTML Canvas (client-side
   interactivity), and when combined with Datashader it can handle
   enormous datasets by pre-rendering them to images in Python
   (server-side). However, in between these two extremes there is a
   range of data sizes that could be addressed well by the client-side
   WebGL technology. Bokeh includes some WebGL support, but it is patchy
   and not fully implemented, so it is not the default for either direct
   Bokeh usage or for Bokeh with the HoloViews API. Volunteers to
   maintain and expand the WebGL support could make a much broader range
   of data sizes practical in easily redistributable standalone HTML
   files, and could enable new classes of high-performance interactive
   features.

2. **Integrating 3D surface and volume rendering into PyViz**: HoloViews
   can plot limited quantities of 3D surface or point data using
   `Matplotlib <//holoviews.org/reference/elements/matplotlib/TriSurface.html>`__
   or
   `Plotly <//holoviews.org/reference/elements/plotly/TriSurface.html>`__,
   but other tools are needed for larger datasets or for volumetric
   rendering with transparent/semitransparent voxels. Improving 3D
   support could be as simple as providing examples for using existing
   tools like
   `IPyVolume <//github.com/maartenbreddels/ipyvolume>`__ and
   `Vaex <//vaex.astro.rug.nl>`__, or by wrapping JavaScript
   libraries like `ThreeJS <//threejs.org>`__ and
   `CesiumJS <//cesiumjs.org>`__.  There's a first `prototype
   for a CesiumJS backend now available <//assets.holoviews.org/demos/HoloViews_CesiumJS.html>`__,
   but lots more work to do to make it practical for real use.

3. **Toolbox for GIS primitives**: The PyViz stack is fully general
   purpose, supporting data of any type, and already has many advantages
   over traditional Earth-specific approaches to dealing with data with
   latitude and longitude coordinates. However, existing GIS packages
   make certain domain-specific functionality simpler, such as computing
   vegetation indexes and other common manipulations of Earth-related
   data. It would be helpful to provide a well-tested collection of
   these common operations built on the PyViz stack so that it can be
   a more "drop-in" replacement for proprietary GIS systems.  Fast
   geographic indexes were already added to Datashader and are
   awaiting documentation (NDVI, slope, aspect, hillshade). Other
   desired features:
   
   - Fast geographic operations for Datashader
       * Zonal statistics for an ROI
           - Percentage area by category
           - Summary stats
       * Hydrology tools
           - Flow accumulation
           - Flow direction
           - Watershed
       * Euclidean distance based on input geometry (lines / polygons / points)
       * Suitability analysis (combining multiple binary aggregates into a yes/no composite)
       * Generate contours from aggregate
       * Calculate viewshed from aggregate
   - Color ramps for showing elevation
   - Bokeh interfaces for external geo data sources (GPX, KML, WMS)
   - Datashader-based WMS Data Server (aggregating an incoming WMS query on demand)

4. **Additional plot types**: HoloViews includes an extensive range of
   plot types (Elements) covering the typical visualizations used across
   many domains. However, there are always more that can be included,
   and some domains are not as well covered as others. Some examples
   that we'd like to include are:

   -  `parallel
      coordinates <//en.wikipedia.org/wiki/Parallel_coordinates>`__
      and `radar charts <//en.wikipedia.org/wiki/Radar_chart>`__
      (polar parallel coordinates, or star charts)
   -  `treemaps <//en.wikipedia.org/wiki/Treemapping>`__
   -  `dendrograms <//en.wikipedia.org/wiki/Dendrogram>`__ and
      `cladograms <//en.wikipedia.org/wiki/Cladogram>`__
   -  `radial trees <//en.wikipedia.org/wiki/Radial_tree>`__
   -  `packed
      bubbles <//stackoverflow.com/questions/46131572/making-a-non-overlapping-bubble-chart-in-matplotlib-circle-packing>`__
   -  `funnel charts <//en.wikipedia.org/wiki/Funnel_chart>`__

   (And if someone wants to write and maintain a `pie chart
   <//en.wikipedia.org/wiki/Pie_chart>`__ even though they are
   nearly always the wrong thing to do, we can probably be convinced
   to allow it. :-)

5. **More extensive documentation about deployment**: PyViz includes a
   tutorial on `deployment using Bokeh
   server <//pyviz.org/tutorial/13_Deploying_Bokeh_Apps.html>`__,
   but there are many other ways to set up live Python-backed plots,
   including creating a Flask server or embedding into Django, along
   with deploying via Heroku or Google Cloud and AWS or via the
   Anaconda Enterprise platform or on
   `MyBinder <//mybinder.org>`__. Documenting and testing these
   possibilities takes time and effort, and any contributions or
   examples that will help people get started and decide between the
   alternatives would be very helpful.

6. **Better native GUI support**: Right now, PyViz focuses exclusively
   on tools that work well in web browsers, because it aims to support
   the entire workflow from initial exploration to delivery of fully
   functional interactive applications to other stakeholders. One
   consequence is that it doesn't currently support the types of
   interactivity provided by Matplotlib when used with its native GUI
   backends like Qt. It should be feasible to make the interactive
   functionality in HoloViews (e.g. streams and DynamicMaps) support
   native GUI apps as well, allowing the same user code to be applied to
   a wider range of use cases.

7. **Altair/Vega/Vega-lite integration**: HoloViews and Bokeh provide
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
   directly with Panel.

8. **hvPlot/HoloViews serialization**: HoloViews uses a declarative design that
   can be represented in a purely textual form, without any Python code.
   An initial implementation allows any Param-based objects (including
   HoloViews objects) to be represented in JSON or YAML, but it needs
   some polishing before it can be put into wide use for saving and
   restoring configurations and layouts.

9. **Better integration with ____**: There are a lot of tools in the
   Python and other scientific software ecosystems that could be
   included in PyViz or made easily usable from it. NetworkX (already
   usable but not fully exploited yet) is just one example of many;
   suggestions welcome!

10. **GUI-based plot creation**: (As in business intelligence and
    dashboarding applications.) The powerful components available
    in PyViz are ready for Python users to put together into
    visualizations and apps, but they would also make a very strong
    base for building a graphical approach for working with data, with
    drag and drop layouts, GUI-configurable mapping of data sources, and
    GUI configuration of the plot objects. HoloViews components are
    already declarative, which means that they can be mapped directly
    into GUI elements for changing their parameters dynamically. Paired
    with the new `Intake <//github.com/ContinuumIO/intake>`_
    library for declaring data sources, it would be possible to build a
    fully graphical interface for working with data that would have the
    advantage of being backed by a fully configurable, open-source set
    of plotting library elements, ensuring that when people outgrow
    the GUI framework they can easily extend and expand anything
    developed in it, unlike current business intelligence and
    dashboarding applications.

If any of the functionality above is interesting to you (or you have
ideas of your own!) and can offer help with implementation, please
open an issue on this repository or on the specific subproject
repository involved. And if you are lucky enough to be in a position
to fund our developers to work on it, please contact
``sales@anaconda.com``.
