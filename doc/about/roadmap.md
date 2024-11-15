# HoloViz Roadmap, as of 11/2024

HoloViz helps coordinate between numerous independent open-source projects, each with its own developers, priorities, and agendas. The future of HoloViz largely depends on a distributed team of developers who focus on the areas of greatest current interest and need, including areas that receive specific funding.

Currently ongoing or scheduled priorities include:

1. **Ongoing maintenance, improved documentation and examples**: Address various bugs and usability issues reported on the issue tracker as time permits.

2. **Better Datashader integration with external plotting libraries (HoloViews, Plotly, Matplotlib)**: Improve integration so external plotting programs can support user-friendly features like hover information, legends, and colorbars.

3. **Support for managing annotations**: Develop annotations as a first-class component in HoloViz tools, allowing users to add annotations to plots and dashboards. See [holonote on GitHub](https://github.com/holoviz/holonote) for progress.

Other goals for HoloViz or packages designed to work well with HoloViz include:

1. **New and improved workflow examples in biomedical and Earth sciences, especially utilizing machine learning**: Provide demonstrations for handling and visualizing large, multidimensional datasets in data-intensive research domains. Examples are available at [Project Pythia](https://projectpythia.org), [holoviz-topics/neuro](https://github.com/holoviz-topics/neuro), and [Panel Gallery](https://panel.holoviz.org/gallery/index.html#app-gallery).

2. **Better deployment and exploration of large-scale visualizations**: Improve automatic generation of tiles for exploring large datasets. See [this notebook](https://github.com/holoviz/datashader/blob/main/examples/tiling.ipynb) for incomplete work on tiling.

3. **Integrating 3D surface and volume rendering into HoloViz**: Improve 3D support for larger datasets and volumetric rendering. Check out [an early prototype for a CesiumJS backend](http://assets.holoviews.org/demos/HoloViews_CesiumJS.html) for progress.

4. **Additional plot types**: Add more plot types, such as:
   - [Parallel coordinates](https://en.wikipedia.org/wiki/Parallel_coordinates) and [radar charts](https://en.wikipedia.org/wiki/Radar_chart)
   - [Treemaps](https://en.wikipedia.org/wiki/Treemapping)
   - [Dendrograms](https://en.wikipedia.org/wiki/Dendrogram) and [cladograms](https://en.wikipedia.org/wiki/Cladogram)
   - [Radial trees](https://en.wikipedia.org/wiki/Radial_tree)
   - [Packed bubbles](https://stackoverflow.com/questions/46131572/making-a-non-overlapping-bubble-chart-in-matplotlib-circle-packing)
   - [Funnel charts](https://en.wikipedia.org/wiki/Funnel_chart)
   - [Donut charts](https://datavizcatalogue.com/methods/donut_chart.html) (which can be modified to make a pie chart)

5. **Interactive Matplotlib plotting**: Expand HoloViews support for interactive Matplotlib output, potentially using ipympl.

6. **Better native GUI support**: Make interactive functionality in HoloViews compatible with native GUI apps, allowing user code to be applied in a wider range of use cases.

7. **Altair/Vega/Vega-lite integration**: Implement a translator between HoloViews/Bokeh and declarative libraries like Altair, Vega, and Vega-Lite to improve interoperability.

8. **hvPlot/HoloViews serialization**: Finalize JSON or YAML serialization for Param-based objects, including HoloViews objects, to allow saving and restoring configurations and layouts.

9. **Independent selection groups**: Introduce support for multiple independent selection groups, allowing each to have its own identity and selection-based actions.

10. **Easy to configure drilldown support**: Implement intuitive drilldown support, possibly through a new API or adaptation of link_selections.

11. **Better integration with other tools**: Enhance HoloViz compatibility with additional tools, such as NetworkX, for broader ecosystem support.

If any of the above functionality interests you, or if you have ideas of your own, please open an issue on this repository or the specific subproject repository involved.
