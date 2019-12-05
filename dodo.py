import os
if "PYCTDEV_ECOSYSTEM" not in os.environ:
    os.environ["PYCTDEV_ECOSYSTEM"] = "conda"

from pyctdev import *  # noqa: api

def task_test_user_install_part1():
    return {'actions':["conda create -y -n holoviz-tutorial python=3.6"]}

def task_test_user_install_part2_conda():
    return {'actions':[
        "conda install -y -c pyviz/label/dev holoviz nbsmoke",
        "holoviz examples --path=. --force --use-test-data",
        # TODO: bokeh sampledata isn't a documented step
        "bokeh sampledata",
        'pytest --nbsmoke-run -k ".ipynb"']}

def task_test_user_install_part2_pip():
    return {'actions':[
        # would need to be documented: "pip users will need to install snappy e.g. via their system packaging tool (how to do this varies between platforms - or use conda)"
        "pip install python-snappy",
        "pip install holoviz nbsmoke",
        "holoviz examples --path=. --force --use-test-data",
        # TODO: bokeh sampledata isn't a documented step
        "bokeh sampledata",
        'pytest --nbsmoke-run -k ".ipynb"']}
