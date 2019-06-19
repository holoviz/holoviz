"""
HoloViz "metamodule" -- Convenience aliases and API imports for HoloViz-related libraries.
"""

import holoviews as hv                                   # noqa (API import)
import numpy as np                                       # noqa (API import)
import pandas as pd                                      # noqa (API import)
import bokeh as bk                                       # noqa (API import)
import param as pm                                       # noqa (API import)
import panel as pn                                       # noqa (API import)
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

__version__ = str(pm.Version(fpath=__file__,archive_commit="$Format:%h$", reponame='holoviz'))

##
# make pyct's example/data commands available if possible
from functools import partial
try:
    from pyct.cmd import copy_examples as _copy, fetch_data as _fetch, examples as _examples
    copy_examples = partial(_copy, 'holoviz')
    fetch_data = partial(_fetch, 'holoviz')
    examples = partial(_examples, 'holoviz')
except ImportError:
    def _missing_cmd(*args,**kw): return("install pyct to enable this command (e.g. `conda install -c pyviz pyct` or `pip install pyct[cmd]`)")
    _copy = _fetch = _examples = _missing_cmd
    def _err(): raise ValueError(_missing_cmd())
    fetch_data = copy_examples = examples = _err
del partial, _examples, _copy, _fetch
##
