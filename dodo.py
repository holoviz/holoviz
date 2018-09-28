import os
if "PYCTDEV_ECOSYSTEM" not in os.environ:
    os.environ["PYCTDEV_ECOSYSTEM"] = "conda"

from pyctdev import *  # noqa: api

# TODO: swap "pyviz examples" in for the separate install & download
# cmds when new packages appear

def task_test_user_install_part1():
    return {'actions':["conda create -y -n pyviz-tutorial python=3.6"]}

def task_test_user_install_part2():
    return {'actions':[
        "conda install -y -c pyviz/label/dev pyviz",
        "conda install -y -c pyviz nbsmoke",
        "pyviz --install-examples .",
        "pyviz --download-sample-data",
        # TODO: bokeh sampledata isn't a documented step
        "bokeh sampledata",
        'pytest --nbsmoke-run -k ".ipynb" --ignore=tutorials/apps']}
