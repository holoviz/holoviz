# Contributing Guide

This is the contrituting guide to HoloViz, and the reference to better understand how the HoloViz project is managed.

## TL;DR



## GitHub

HoloViz consists of a number of Python projects. All these projects are version-controlled with [Git]() and hosted on GitHub. Having all the projects hosted on GitHub means that we can use all the nice features it freely provides to open-source projects, including easy collaboration through issues and pull requests, continuous integration (CI) with GitHub Actions and documentation hosting with GitHub Pages. Yet it is important to keep in mind that nothing lasts forever and that at some point HoloViz may be forced to rely on other platform(s)/service(s), the more HoloViz relies on GitHub the more difficult any transition to another system.

The HoloViz group owns a few GitHub organizations. The main one where you are likely to want to contribute is [holoviz](https://github.com/holoviz/), it hosts the core packages maintained by the group. HoloViz was previously named `PyViz` but the Python community suggested that it wasn't that appropriate and as such the group was renamed HoloViz, inspired by HoloViews. This is why the two other organisations owned by the group, [pyviz-dev](https://github.com/pyviz-dev/) and [pyviz-topics](https://github.com/pyviz-topics/), have *pyviz* in their name. [pyviz-dev](https://github.com/pyviz-dev/) hosts two main types of repositories. First, it hosts packages that support maintaining the core HoloViz packages. This includes for instance `nbsite` which is a tool to build sphinx-based websites from notebooks. These support packages were developped when no alternative, or satisfying alternative, was available at the time they were needed by the group. Interestingly these packages could have become pretty popular had they been more promoted, however it was never a goal for the group which was instead focusing on improving data vizualisation with Python rather than on improving the Python tooling. Second, *pyviz-dev* hosts repositories that are only used to host *dev* builds of the core packages websites, i.e. no actual work is done on these repositories, they just get updated automatically in a CI process. [pyviz-topics](https://github.com/pyviz-topics/) hosts repositories that demonstrate concrete usage of the HoloViz tools.

* [holoviz](https://github.com/holoviz/)
    * [holoviz](https://github.com/holoviz/holoviz): HoloViz website and tutorial
    * [hvPlot](https://github.com/holoviz/hvplot): A high-level plotting API for pandas, dask, xarray, and networkx built on HoloViews
    * [Panel](https://github.com/holoviz/panel): A high-level app and dashboarding solution for Python
    * [Lumen](https://github.com/holoviz/Lumen): Illuminate your data.
    * [HoloViews](https://github.com/holoviz/holoviews): With Holoviews, your data visualizes itself.
    * [GeoViews](https://github.com/holoviz/geoviews): Simple, concise geographical visualization in Python
    * [Datashader](https://github.com/holoviz/datashader): Quickly and accurately render even the largest data.
    * [Colorcet](https://github.com/holoviz/colorcet): A set of useful perceptually uniform colormaps for plotting scientific data
    * [Param](https://github.com/holoviz/param): Make your Python code clearer and more reliable by declaring Parameters
    * [Spatialpandas](https://github.com/holoviz/spatialpandas): Pandas extension arrays for spatial/geometric operations
    * [pyviz_comms](https://github.com/holoviz/pyviz_comms): Bidirectional communication for the HoloViz ecosystem
    * [jupyter-panel-proxy](https://github.com/holoviz/jupyter-panel-proxy): Jupyter Server Proxy for Panel
* [pyviz-dev](https://github.com/pyviz-dev/)
    * [nbsite](https://github.com/holoviz/nbsite): Build a tested, sphinx-based website from notebooks
    * [nbsmoke](https://github.com/pyviz-dev/nbsmoke): Basic notebook checks. Do they run? Do they contain lint?
    * [pyctdev](https://github.com/pyviz-dev/pyctdev): Python packaging Common Tasks for Developers
    * [autover](https://github.com/pyviz-dev/autover): Provides consistent and up-to-date version strings for Python packages. 
    * [pyct](https://github.com/pyviz-dev/pyct): Python packaging Common Tasks
    * [blog](https://github.com/pyviz-dev/blog): The HoloViz blog
    * [status-dashboard](https://github.com/pyviz-dev/status-dashboard): Status Dashboard for HoloViz Project
    * [pyviz-dev.github.io](https://github.com/pyviz-dev/pyviz-dev.github.io): Index of all sites on pyviz-dev
    * [holoviz_tasks](https://github.com/pyviz-dev/holoviz_tasks): Shared GHA workflows and tasks used to maintain the HoloViz repositories
    * more ...
* [pyviz-topics](https://github.com/pyviz-topics/)
    * [examples](https://github.com/pyviz-topics/examples): 
    * [earthsim](https://github.com/pyviz-topics/earthsim):
    * [earthml](https://github.com/pyviz-topics/earthml):
    * [holodoodler](https://github.com/pyviz-topics/holodoodler):
    * more ...


Additionally the HoloViz group maintains the [pyviz]() organisation which 

## Repository structure

The core packages have their repository that except in a few cases all share the same structure:

* the tests are nested under the package directory, e.g. at `panel/tests`. The tests are then automatically bundled in the source distribution which makes it a little easier for repackagers to run the tests
* the `examples` and the `doc` folder share the same structure, e.g. you will find `panel/doc/user_guide`  and `panel/examples/user_guide`. The `examples` folder contains [Jupyter Notebooks]() while the `doc` folder usually contains *RestructuredText* and/or *Markdown* files. Check out the [documentation]() section to : TODO: pyct?
* the `.github` directory contains GitHub specific configuration files, e.g. for GitHub Actions.
* optional: the `conda.recipe` directory contains a conda recipe template that is used by the building tooling when creating a conda package.
* optional: the `binder` directory contains configuration files to setup [binder]()

## Conda

The HoloViz group relies heavily on the [conda package manager](https://conda.io/docs/intro.html) for the following reasons:

* the HoloViz group consists of people who have a scientific background. Installing the Python scientific libraries was a difficult task to achieve with `pip` as these libraries usually depend on binary dependencies that need to be compiled. `conda` was created to solve this exact problem and the HoloViz group was an early user of this solution. While it's important to note that installing scientific libraries with `pip` has become a smoother experience (notably thanks to more wheels being distributed), installing some packages like those of the Python geo-stack (`rasterio`, `pyproj`, etc.) still proves to be challenging and `conda` *usually* provides a better experience in that case.
* the core maintainers of the HoloViz group are employed by [Anaconda]() and as such it makes sense for the group to use a tool developed by the company
* some HoloViz-maitained packages such as Panel require softwares like `nodejs` that cannot be installed with `pip` while they can be installed with `conda`. `conda` allows to create a complete dev environment without having to install other softwares from another way (e.g. with `brew` on MacOS).

So for you when it comes to contributing to HoloViz we **recommend** that you start with installing `conda` if it's not already installed. You would have a closer experience to those of the maitainers and they will be in a better position to help you setting up your dev environment and debug whatever issue you may encounter.

To install Conda on any platform, see the [Download conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html) section of the [conda documentation](https://conda.io/docs/index.html).

Of course this is not a strict requirement and you can definitely decide to use `pip` instead!

## Pyctdev

[pyctdev]() stands for *python packaging common tasks for developers*, it is a developer tool built by the HoloVIz group in an attempt to simplify managing Python projects, by providing a way to declare how to run the usual tasks required to maintain a project, such as running its unit tests or building its documentation, and by standardizing the way to execute these tasks with e.g. `doit test_unit` or `doit build_website`. `pyctdev` relies on [doit]() to provide a command-line interface to developers (e.g. `doit test_unit`) and can be as such seens as an extension of `doit`. `doit` allows to register *tasks* that consist of a sequence of *actions*, an action being either a command line instruction (e.g. `flake8 .`) or the execution of a Python function. `pyctdev` comes with various common Python tasks dedicated to manage a project, such as the `develop_install` task (executed with `doit develop_install`) that will install the project in development mode with its optional development dependencies.

By unifying the way to execute these common tasks, `pyctdev` makes it easier to work across the HoloViz projects. It also make it easier to work across environments, as the commands to execute should be the same whether you execute them locally or in a CI environment. In addition `pyctdev` supports developing with either pip or conda, which is a unique feature. In practice however `pyctdev` is an ambitious project and while it has proven useful to the HoloViz group it is yet another tool to learn for contributors and to maintain for the group. We still **recommend** that you use `pyctdev` to have a development experience that is closer to the one of the core maintainers. If however you feel constrained by the tooling abstraction that is `pyctdev` you can always ignore it and reach out to the tools you are most comfortable with. In that case you will have to inspect the files of the project you are contributing to to find what tasks you need to run. In each core HoloViz repository you will find a few files that are of importance for `doit/pyctdev`:

* `dodo.py` is a Python module that allows to add per-project `doit` tasks, refer to [its documentation]() to learn how to add or modify a task. A quick way to identify a task is to find a Python function that is names `task_something`, `doit` makes it then available as a command line subcommand with `doit something`.
* `setup.py` is the classic install file of the [setuptools]() build backend, in this file you will find:
    * the list of the runtime dependencies required by the package in the `install_requires` key
    * multiple extra dependency groups required to run different tasks in the `extras_require` key, for instance the `doc` extra group would like the dependencies required to build the documentation site
    * in the `extras_require` key you will also find the dependencies required at the *build* time, with for instance `setuptools` declared in that list
* `tox.ini` is the configuration file of [tox](), `pyctdev` creates tasks out of the commands it contains, and use `tox` directly in some cases (it vendors a version of it).

Now that the main files are defined, we can go through each step of a typical workflow with `pyctdev`, assuming that you are in a cloned repository:

* `conda install -c pyviz/label/dev pyctdev`: to start things off you need to install `pyctdev`, it is available on the `pyviz` channel and we recommend installing a dev release from the dev channel `pyviz/label/dev` to get a more up-to-date version
* `doit env_create -c pyviz -c conda-forge --python=3.8 --name=my_dev_env`: once `pyctdev` is installed you can run the `env_create` command to create a conda environment that will have the Python version and the name you precise, and will fetch packages from the channels you list 
* `conda activate my_dev_env`: to activate the environment you've just created
* `doit -c pyviz -c conda-forge develop_install -o tests -o examples`: the `develop_install` executes three actions, (1) it installs the *build* dependencies (including e.g. `setuptools`), (2) it installs the *runtime* dependencies and the extra dependencies that are listed with the `-o` flag (in the example that would be the *tests* and *examples* groups of dependencies), and (3) it installs the package you're working on in *editable* mode (with `pip install --no-deps --no-build-isolation -e .`).
* `doit test_flakes` (or sometimes `doit test_lint`): run linters on the project code source, e.g. with `flake8`
* `doit test_unit`: run the Python unit tests, i.e. the tests you will find in the `/tests` folder, most likely with `pytest`
* `doit test_examples`: run the *examples*, i.e. the notebooks you will find in the `/examples` folder

## Documentation

Most of the packages maitained by the HoloViz group have a website. Only those that are not promoted for usage outside of the group don't, such as `pyctdev`. HoloViz being dedicated to making data visualization simpler in Python, it made sense for the group to come up with a way to generate websites out of a collection of Jupyter Notebooks. As a consequence [nbsite](https://github.com/pyviz-dev/nbsite) was created to achieve that goal. `nbsite` is based on [sphinx](https://www.sphinx-doc.org/en/master/) and is the tool used by all the projects to build their site. Building a site with `nbsite` is usually a two-step process:

* running `nbsite generate-rst ...` will 

## Monitoring

* status dashboard
* cron GH actions
* lumen monitor
* No google analytics

## Deployment

S3, AE5

## Testing

nbsmoke (nbval, nbqa), pytest

## Tooling

## Distribution

pyviz channel, pip

## Communication

Gitter, Discourse, GitHub, HoloViz meetings and Hackmd
Github Teams
Github accounts: like https://github.com/holoviz-developers and https://github.com/pyviz-developers
