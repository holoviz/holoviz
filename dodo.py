import os
if "PYCTDEV_ECOSYSTEM" not in os.environ:
    os.environ["PYCTDEV_ECOSYSTEM"] = "conda"

from pyctdev import *  # noqa: api

def task_test_user_install_part1():
    return {'actions':["conda create -y -n pyviz-tutorial python=3.6"]}

def task_test_user_install_part2():
    return {'actions':[
        "conda install -y -c pyviz/label/dev pyviz",
        "conda install -y -c pyviz nbsmoke",
        "pyviz examples --path=.",
        # TODO: bokeh sampledata isn't a documented step
        "bokeh sampledata",
        'pytest --nbsmoke-run -k ".ipynb" --ignore=tutorials/apps']}
