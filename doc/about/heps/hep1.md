# HEP 1 - Python Version Support

<table>
<tr><td> Identifier </td><td> HEP 1 </td></tr>
<tr><td> Title </td><td> Python Version Support </td></tr>
<tr><td> Status </td><td> Accepted </td></tr>
<tr><td> Author(s) </td><td> Ian Thomas </td></tr>
<tr><td> Created </td><td> April 19, 2023</td></tr>
<tr><td> Accepted </td><td> May 23, 2023</td></tr>
<tr><td> Last Updated </td><td> March 18, 2025</td></tr>
<tr><td> Discussion </td><td> https://github.com/holoviz/holoviz/pull/362 </td></tr>
<tr><td> Implementation </td><td> NA </td></tr>
</table>


> Note: HEP 1 was updated on March 15, 2024 by Demetris Roumis to align with the updated HEP format, proposed by HEP 0. Notably, he added the table above and the 'Resolution' section below. If there is any discrepency between the reformatted HEP 1 and the original HEP 1, the original HEP 1 takes precedence.

> Note: HEP 1 was updated on March 18, 2025 by Maxime Liquet to specify that projects must not drop support for an old Python version in a patch release.


## Summary

This enhancement proposal describes the possible policy that HoloViz projects
might adopt for support of Python versions.

## Resolution

The community decided to adopt a Python version support policy for HoloViz projects that aims to support as many active Python releases as reasonably possible, with specific policies tailored for projects with few dependencies, those tightly coupled to Bokeh, and those with geospatial dependencies, ensuring alignment with dependent libraries' support cycles.

## Background

Historically a new version of Python has been released every one to two years,
and in future annual releases are planned every October. The lifespan of each
version is typically five years, so on any particular date there are expected
to be five active Python versions. The current status of Python versions is
illustrated in the
[Python Developer's Guide](https://devguide.python.org/versions).

NumPy have a more restrictive policy of supporting Python version released in
the last 42 months (three and a half years), with a few extra caveats, in
[NEP29](https://numpy.org/neps/nep-0029-deprecation_policy.html). They
therefore support the latest three to four Python releases.

A number of projects in the scientific Python ecosystem follow the NumPy policy
including

- [Matplotlib](https://matplotlib.org/stable/devel/min_dep_policy.html)
- [numba](https://numba.readthedocs.io/en/stable/release-notes.html#version-0-47-0-jan-2-2020)
- [pandas](https://pandas.pydata.org/pandas-docs/stable/development/policies.html)
- [xarray](https://xarray.pydata.org/en/v2023.04.0/getting-started-guide/installing.html#minimum-dependency-versions)

Bokeh, a library of particular importance to HoloViz, has a
[policy](https://github.com/bokeh/bokeh/wiki/BEP-9:-Downstream-Version-Support)
to support at least the latest three versions of Python so although it does not
explicitly follow NumPy's policy it is similar.

At the time of writing in mid April 2023, Python versions currently supported
are 3.7 to 3.11. 3.7 reaches end of life at the end of June, and Python 3.12
will be released in October. NumPy's previous release (1.24.2) supported Python
3.8 to 3.11 and the next release will support 3.9 to 3.11. Bokeh's most recent
release (3.1.0) supported Python 3.8 to 3.11, and the next release (3.2.0) will
support Python 3.9 to 3.11.

## Specification/Policy


Ideally HoloViz projects should support as many Python releases as are
reasonably possible. Support for a new Python release should ideally occur on
the day of release, but the limiting factor here is often numba as that is
usually delayed.

Support for old versions of Python is limited, in a practical sense, by
dependent libraries' support for old versions. Dependencies that have a slow
change cadence are usually not a problem, but those with a fast change cadence
(e.g. pyarrow) or with major backward-breaking changes (e.g. Bokeh 3.0, pandas
2.0) potentially are. A desire to support older versions of Python here can
result in HoloViz projects effectively performing the integration testing,
fixes and workarounds for those dependencies that have already dropped support
for older Python.

In deciding on a policy for support of old Python releases, the HoloViz
projects can be divided into three groups:

1. Colorcet and Param: projects with few dependencies.
2. Panel, Lumen, HoloViews, hvPlot and Datashader: Panel is tightly coupled to
Bokeh, and the other projects here are commonly used in Panel so they should
also be considered tightly coupled to Bokeh.
3. GeoViews and SpatialPandas: projects with geospatial dependencies (install
or CI).

For 1, the limited dependencies means that support can be for all Python
releases that are currently active.

For 2, the tight coupling with Bokeh means that Bokeh's policy should be
followed. However, this can be relaxed slightly so that following a Bokeh
release that drops support for a particular Python version each of the HoloViz
projects will make one further release supporting that Python version before
dropping it themselves.

For 3 the geospatial dependencies often cause problems by not being available
as wheels on PyPI and being difficult to resolve on conda. The HoloViz policy
should be the same as that of 2 above for uniformity.

The HoloViz projects must not drop support for an old Python version in a patch
release, but in a minor or major release.

## Illustration 

To illustrate the proposed policy, this is what it means for the remainder of
2023.

All projects currently support Python 3.11 and will support Python 3.12 when it
is released in October or as soon as possible after that.

Colorcet and Param currently support Python 3.7 upwards. When this reaches end
of life at the end of June, the minimum support Python version will increase to
3.8 for their next releases.

The current Bokeh release (3.1.0) supports minimum Python of 3.8 and the next
release (3.2.0) will support minimum Python 3.9. All HoloViz projects (except
Colorcet and Param which are covered above) should
drop support for Python 3.7 as soon as possible to support a minimum Python of
3.8. Following release of Bokeh 3.2.0 there should be one further release per
HoloViz project that supports Python.

## Copyright
This document is placed in the public domain or under the CC0-1.0-Universal license, whichever is more permissive.
