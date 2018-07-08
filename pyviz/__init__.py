"""
PyViz "metamodule" -- Convenience aliases and API imports for PyViz-related libraries.
"""

import holoviews as hv                                   # noqa (API import)
import numpy as np                                       # noqa (API import)
import pandas as pd                                      # noqa (API import)
import bokeh as bk                                       # noqa (API import)
import param as pm                                       # noqa (API import)
import parambokeh as pb                                  # noqa (API import)
import xarray as xr                                      # noqa (API import)
import colorcet as cc                                    # noqa (API import)
import datashader as ds                                  # noqa (API import)
import datashader.transfer_functions as tf               # noqa (API import)
import holoviews.operation.datashader as hd              # noqa (API import)
import dask.dataframe as dd                              # noqa (API import)

# Some libraries are loaded only if present; will raise error if used but not importable
# Should consider making them fully lazily imported as well
try:
    import geoviews as gv                                # noqa (API import)
except ImportError:
    pass

from holoviews import help                               # noqa (API import)

__version__ = str(pm.Version(fpath=__file__,archive_commit="$Format:%h$", reponame='pyviz')
