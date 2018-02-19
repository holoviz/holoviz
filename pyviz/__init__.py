"""
PyViz "metamodule" -- Convenience aliases and API imports for PyViz-related libraries.
"""

import holoviews as hv                                   # noqa (API import)
import numpy as np                                       # noqa (API import)
import pandas as pd                                      # noqa (API import)
import param as pm                                       # noqa (API import)
import xarray as xr                                      # noqa (API import)
import datashader as ds                                  # noqa (API import)
import datashader.transfer_functions as tf               # noqa (API import)
import holoviews.operation.datashader as hd              # noqa (API import)

# Some libraries are loaded only if present; will raise error if used but not importable
# Should consider making them fully lazily imported as well
try:
    import geoviews as gv                                # noqa (API import)
except ImportError:
    pass

from holoviews import help                               # noqa (API import)

__version__ = pm.Version(release=(1,9,2), fpath=__file__, commit="$Format:%h$", reponame='pyviz')


