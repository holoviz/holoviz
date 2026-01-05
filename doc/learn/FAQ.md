# FAQ

## What is HoloViz, really?

HoloViz is about working together on many different levels:

- A set of high-level packages that make it easier to use plotting and data libraries -- good starting points for doing your work!
- A set of package authors who work together to make their packages interoperate well, to help reduce gaps and duplication between packages and improve the overall user experience.
- A set of packages that have been verified to work well together, in matching versions, and are continuously tested to ensure that they keep working together.
- A set of examples and tutorials that help you see how various Python packages can work together to solve a huge range of visualization problems, from common situations to tricky special cases.


## How does HoloViz relate to PyViz?

The packages in HoloViz were originally described as "PyViz" packages, but in June 2019 PyViz.org was split off as a separate general-purpose site for all of Python visualization, with HoloViz referring to the specific packages maintained by the group now called HoloViz.

## Is HoloViz a commercial product?

HoloViz is supported by [Anaconda, Inc.](https://anaconda.com) and through partnerships with a number of commercial and government clients, but HoloViz and all of its component packages are open source packages fully and freely available for both commercial and non-commercial use.

## Wow, how did you do all this work?

HoloViz is built on a wide foundation of libraries and tools in the scientific Python ecosystem. Most of the time, we're just pulling together existing functionality and making it simpler to access and easier to compose. We do have some projects like Datashader and Colorcet that were explicitly commissioned to fill a need (in this case, handling large data and providing a range of uniform colormaps), but mostly the underlying functionality was always there, it was just difficult to apply to typical situations in data science and analysis.

## Does HoloViz include 3D support?

A bit. Some historical context will probably help make this clear. Over the past 30 years or so, visualization packages and developers have been organized into two mostly non-overlapping camps dealing with either [scientific visualization](https://en.wikipedia.org/wiki/Scientific_visualization) or [information visualization](https://en.wikipedia.org/wiki/Information_visualization). SciVis primarily focuses on data that is situated in the 3D space of the real world, and it thus uses variants of the three-dimensional rendering algorithms made to represent the real world in computer graphics. InfoVis primarily focuses on representing more abstract information that can be laid out in any number of ways, and for practical reasons, it tends to use 2D representations where it is simple to show axes and other tools to explicitly indicate mappings from the page onto the underlying data coordinates.

HoloViews and hvPlot currently focus on the packages and applications from the InfoVis domain, and thus primarily support two-dimensional plotting and layouts. There is some limited three-dimensional rendering in HoloViz provided by [Matplotlib](https://holoviews.org/reference/elements/matplotlib/TriSurface.html) and [Plotly](https://holoviews.org/reference/elements/plotly/TriSurface.html), but HoloViews does not currently include comprehensive support for 3D visualizations, virtual reality, augmented reality, and related topics. See the [HoloViz Roadmap](../about/roadmap) if you would like to help broaden its coverage of these topics, or else consider using complementary packages like [MayaVi](https://docs.enthought.com/mayavi/mayavi), [VTK](https://www.vtk.org/), [IPyVolume](https://github.com/maartenbreddels/ipyvolume), and [Vaex](https://vaex.io/docs/index.html) (a 3D-capable version of Datashader). Several of those tools can be used with Panel, which can help you integrate 3D visualizations from other sources into your HoloViz layout or application.

## What else is *not* covered well by HoloViz?

- Native GUI apps (mostly only browser-based approaches are included so far)
- Domain-specific toolkits and analyses (not suitable for HoloViz, but can be in affiliated repos)
- Native JavaScript toolkits like D3 (HoloViz focuses on people who want to work directly in Python, not those willing to write code in other languages to deal with their Python data)
- Hard real-time displays (HoloViz tools offer dynamic updates, but cannot enforce strict latency requirements)

See the [Roadmap](../about/roadmap) for more details on topics that could be added in future work.

## How do I report a problem?

For the quickest response from those who can fix things, try to identify which HoloViz package is most directly involved, and then click on the appropriate logo on the [HoloViz home page](../index) to find their Github site for filing issues. If your issue is with this website or the notebooks you downloaded from it or if it covers multiple HoloViz projects, then please open an issue on [github.com/holoviz](https://github.com/holoviz/holoviz/issues). And if you want to start open-ended discussion or you can't figure out which project is involved, visit [discourse.holoviz](https://discourse.holoviz.org).
