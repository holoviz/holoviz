***
FAQ
***

What is PyViz, really?
======================

PyViz is about working together on many different levels:

- A set of high-level packages that make it easier to use plotting and data libraries -- good starting points for doing your work!
- A set of package authors who work together to make their packages interoperate well, to help reduce gaps and duplication between packages and improve the overall user experience.
- A set of packages that have been verified to work well together, in matching versions, that can all be installed with one command and are continuously tested to ensure that they keep working together
- A set of examples and tutorials that help you see how various Python packages can work together to solve a huge range of visualization problems, from common situations to tricky special cases.

There is a specific installable package named ``pyviz``, but it's valuable mainly for its dependencies, which are installed in matching versions when ``pyviz`` is installed.  There is almost no code actually in PyViz, apart from the examples in the tutorials.


Is PyViz a commercial product?
==============================

PyViz is supported by `Anaconda, Inc. <//anaconda.com>`_ and through partnerships with a number of commercial and government clients, but PyViz and all of its component packages are open source packages freely available for both commercial and non-commercial use.


Wow, how did you do all this work?
==================================

PyViz is built on a wide foundation of libraries and tools in the scientific Python ecosystem. Most of the time, we're just pulling together existing functionality and making it simpler to access and easier to compose. We do have some projects like Datashader and Colorcet that were explicitly commissioned to fill a need (in this case, handling large data and providing a range of uniform colormaps), but mostly the underlying functionality was always there, it was just difficult to apply to typical situations in data science and analysis.

Does PyViz include 3D support?
==============================

A bit. Some historical context will probably help make this clear. Over the past 30 years or so, visualization packages and developers have been organized into two mostly non-overlapping camps dealing with either `scientific visualization <//en.wikipedia.org/wiki/Scientific_visualization>`__ or  `information visualization <//en.wikipedia.org/wiki/Information_visualization>`__. SciVis primarily focuses on data that is situated in the 3D space of the real world, and it thus uses variants of the three-dimensional rendering algorithms made to represent the real world in computer graphics. InfoVis primarily focuses on representing more abstract information that can be laid out in any number of ways, and for practical reasons it tends to use 2D representations where it is simple to show axes and other tools to explicitly indicate mappings from the page onto the underlying data coordinates.

PyViz currently focuses on the packages and applications from the InfoVis domain, and thus primarily supports two-dimensional plotting and layouts. There is some limited three-dimensional rendering in PyViz provided by `Matplotlib <//holoviews.org/reference/elements/matplotlib/TriSurface.html>`__ and `Plotly <//holoviews.org/reference/elements/plotly/TriSurface.html>`__, but PyViz does not currently include comprehensive support for 3D visualizations, virtual reality, augmented reality, and related topics. See the `PyViz Roadmap <Roadmap>`_ if you would like to help broaden its coverage of these topics, or else consider using complementary packages like `MayaVi <//docs.enthought.com/mayavi/mayavi>`__, `VTK <//www.vtk.org/>`__, `IPyVolume <//github.com/maartenbreddels/ipyvolume>`__, and `Vaex <//vaex.astro.rug.nl>`__ (a 3D-capable version of Datashader).


What else is *not* covered well by PyViz?
=========================================

- Native GUI apps (only browser-based approaches are included so far)
- Domain-specific toolkits and analyses (not suitable for PyViz, but can be in affiliated repos)
- Native JavaScript toolkits like D3 (PyViz focuses on people who want to work directly in Python, not those willing to write code in other languages to deal with their Python data)
- Hard real-time displays (PyViz tools offer dynamic updates, but cannot enforce strict latency requirements)
- Drag and drop visualization development (PyViz supports extensive interactivity, but does not currently have a way to build non-trivial visualizations graphically as in business intelligence apps or spreadsheets)

See the `Roadmap <Roadmap>`_ for more details on topics that could be added in future work.


How do I report a problem?
==========================

For the quickest response from those who can fix things, try to identify which PyViz package is most directly involved, and then click on the appropriate logo on the `PyViz home page <index.html>`_ to find their Github site for filing issues.  If you can't figure out which project is involved, or if your issue is with this website, the notebooks you downloaded from it, or the ``pyviz`` package itself, then please open an issue on `github.com/pyviz. <//github.com/pyviz/pyviz/issues>`_ or chat with us on the `Gitter channel for HoloViews. <//gitter.im/pyviz/pyviz>`_
