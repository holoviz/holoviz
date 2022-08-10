# Contributing Guide

This guide includes general guidelines on how to contribute to HoloViz. Read the [Operating Guide](TODO) if you are interested to learn how an Open-Source project like HoloViz operates.

## Why contributing?

There are many reasons why you could contribute to the HoloViz project, including:

* You appreciate the HoloViz project, its mission and values, and would like to help
* You are a user of one of the HoloViz packages and need a bug to be fixed or a new feature to be implemented, and you are willing to tackle that
* You are looking for some open-source experience
* You have been reading one of the HoloViz website and found something to improve, even just a simple typo
* ...

These reasons, and whatever reason brought you here, are all valid to our eyes. We **welcome anyone** who wish to contribute, and as you will see there are **many** ways to contribute!

```{hint}
Contributing to the HoloViz project could even get you a **job**, this has been the case for a couple of HoloViz members.
```

## What and how to contribute?

### Documentation

Each core HoloViz package has its own website, maintaining the content on these websites is a lot of work, and you can easily help by:

* submitting a PR to fix a typo
* submitting a PR to clarify a section
* submitting a PR to document an undocumented feature
* submitting a PR to update a section that should have been updated
* ...

How the websites look and feel can also be improved, if you happen to have some front-end skills, your help would be greatly appreciated.

Finally the documentation also lies within the code, and in Python it is found in the so-called *docstrings* that accompany modules, classes, methods and functions. You can easily improve the docstrings by:

* submitting a PR to fix a typo
* submitting a PR to clarify a definition
* submitting a PR to fix or document the default value of a parameter
* ...

```{tip}
Documentation fixes/improvements that are of a small scope usually do not need an issue to be opened before hand. If you don't have the time to open a PR, we would appreciate if you could at least record your suggestion in an issue, that would already be a very nice contribution!
```

### Support

HoloViz users are recommended to ask their questions on the [HoloViz Discourse Forum](https://discourse.holoviz.org/). This forum is only useful if questions can find answers, and you can be the one writing that answer that will make somebody else's life so much easier! The HoloViz team members monitor the forum and try to regularly contribute to it, yet the more we are, the better.

```{tip}
Answering questions on the HoloViz Discourse Forum, or even just trying to answer some random questions, is a very good way to learn how to use the HoloViz tools.
```

Some users also ask questions on [StackOverflow](TODO), which isn't much monitored by the HoloViz team so we would greatly appreciate any help there. 

### Outreach

Before addressing how to contribute code to HoloViz, it is important to mention that a very useful way to contribute to HoloViz is by communicating more about it. 

### Code


## How to contribute?

## TL;DR

TODO

## Operating guide

The HoloViz project consists of:

* a number of core packages (including Panel, Lumen, HoloViews, GeoViews, Datashader, hvPlot, Colorcet, Param. that need to be maintained, tested, documented, etc.
* a group of people collaborating to make the project better

This section of the guide describes how that system works.


### PyViz

The HoloViz project was previously named `PyViz` but the Python community suggested that it wasn't that appropriate and as such PyViz was renamed HoloViz, inspired by HoloViews. As renaming is a lot of work, and that it can 
potentially break some systems, you will still find references to PyViz here and there.

PyViz, or [PyViz.org](https://pyviz.org/), is a project of its own and is a fully open guide to all Python visualization tools. The HoloViz group maintains the [pyviz](https://github.com/pyviz) organisation, but only for historical reasons, at it is meant to be shared by the whole Python visualization community.

### GitHub

#### Organisations and repositories

HoloViz consists of a number of Python projects. All these projects are version-controlled with [Git]() and hosted on GitHub. Having all the projects hosted on GitHub means that HoloViz can rely on all the nice features it freely provides to open-source projects, including easy collaboration through *Issues and Pull Requests (PR)*, continuous integration (CI) with *GitHub Actions (GHA)* and documentation hosting with *GitHub Pages*.


```{warning}
It is important to keep in mind that nothing lasts forever and that at some point HoloViz may be forced to rely on other platform(s)/service(s), the more HoloViz relies on GitHub the more difficult any transition to another system.
```

The HoloViz group owns a few GitHub organizations:

* [holoviz](https://github.com/holoviz/) is the main one and where you are likely to want to contribute. It hosts the core packages maintained by the group.
* [pyviz-dev](https://github.com/pyviz-dev/) hosts two main types of repositories:
    * Packages that support maintaining the core HoloViz packages, including for instance `nbsite`, `nbsmoke`, `pyctdev`, `pyct` and `autover`. These support packages were developped when no alternative, or satisfying alternative, was available at the time they were needed by the group. Interestingly a few of these packages could have become pretty popular had they been more promoted, however it was never a goal for the group which was instead focusing on improving data vizualisation with Python rather than on improving the Python tooling.
    * Repositories that are only used to host *dev* builds of the core packages websites, i.e. no actual work is done on these repositories, they just get updated automatically in a CI process. 
* [pyviz-topics](https://github.com/pyviz-topics/) hosts repositories that demonstrate concrete usage of the HoloViz tools.
* [holoviz-demos](https://github.com/holoviz-demos/) hosts some demos, mostly Panel apps (TODO: are these actually used?)
* [holoviz-community](https://github.com/holoviz-community/) is a place for the HoloViz community to host repositories that are going to be nicely exposed under the HoloViz umbrella

In more details:

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

#### Teams

The `holoviz` organisation has two teams:

* `holoviz-dev`: Team that will manage the HoloViz contents
* `Triaging team`: Contributors able to triage open issues on HoloViz projects

The `pyviz-dev` organisation has one team:

* `pyviz-dev`: PyViz Developers

The `pyviz-topics` organisation has one team:

* `pyviz-dev`: Developers on PyViz Topics

#### Developer account

* [HoloViz Developers](https://github.com/holoviz-developers): Account to use for automated actions on HoloViz projects
* [PyViz Developers](https://github.com/pyviz-developers)

### Repository structure

The core packages have their repository that, except in a few cases, all share the same structure:

* the tests are nested under the package directory, e.g. at `panel/tests`. The tests are then automatically bundled in the source distribution which makes it a little easier for repackagers to run the tests
* the `examples` and the `doc` folder share the same structure, e.g. you will find `panel/doc/user_guide`  and `panel/examples/user_guide`. The `examples` folder contains Jupyter Notebooks while the `doc` folder usually contains *RestructuredText* and/or *Markdown* files. Check out the [documentation]() section to : TODO: pyct?
* the `.github` directory contains GitHub specific configuration files, e.g. for GitHub Actions.
* optional: the `conda.recipe` directory contains a conda recipe template that is used by the building tooling when creating a conda package.
* optional: the `binder` directory contains configuration files to setup [binder]()

### Tooling

#### Conda

The HoloViz group relies heavily on the [conda package manager](https://conda.io/docs/intro.html) for the following reasons:

* the HoloViz group consists of people who have a scientific background. Installing the Python scientific libraries was at some point a very difficult task to achieve with `pip` as these libraries usually depend on binary dependencies that need to be compiled, step that pip delegates to whatever tool is installed on your machine. `conda` was created to solve this exact problem and the HoloViz group was an early user of this solution. While it's important to note that installing scientific libraries with `pip` has become a smoother experience (notably thanks to more wheels being distributed), installing some packages like those of the Python geo-stack (`rasterio`, `pyproj`, etc.) still proves to be challenging and `conda` *usually* provides a better experience.
* the core maintainers of the HoloViz group are employed by [Anaconda](https://www.anaconda.com/) and as such it makes sense for the group to use `conda`
* some HoloViz-maitained packages such as Panel require softwares like `nodejs` that cannot be installed with `pip` while they can be installed with `conda`. `conda` allows to create a complete dev environment without having to install other softwares from another way (e.g. with `brew` on MacOS).

To contribute to HoloViz we **recommend** that you use `conda`. You would have a closer experience to those of the maitainers and they will be in a better position to help you setting up your dev environment and debug whatever issue you may encounter.

To install Conda on any platform, see the [Download conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html) section of the [conda documentation](https://conda.io/docs/index.html).

Of course this is not a strict requirement and you can definitely decide to use `pip` instead!

#### Pyctdev

[pyctdev]() stands for *python packaging common tasks for developers*, it is a developer tool built by the HoloViz group in an attempt to simplify managing Python projects, by providing a way to declare how to run the usual tasks required to maintain a project, such as running its unit tests or building its documentation, and by standardizing the way to execute these tasks with e.g. `doit test_unit` or `doit build_website`. `pyctdev` relies on [doit]() to provide a command-line interface to developers (e.g. `doit test_unit`) and can be as such seen as an extension of `doit`. `doit` allows to register *tasks* that consist of a sequence of *actions*, an action being either a command line instruction (e.g. `flake8 .`) or the execution of a Python function. `pyctdev` comes with various common Python tasks dedicated to manage a project, such as the `develop_install` task (executed with `doit develop_install`) that will install the project in development mode with its optional development dependencies.

By unifying the way to execute these common tasks, `pyctdev` makes it easier to work across the HoloViz projects. It also make it easier to work across environments, as the commands to execute should be the same whether you execute them locally or in a CI environment. In addition `pyctdev` supports developing with either pip or conda, which is a unique feature. In practice however `pyctdev` is an ambitious project and while it has proven useful to the HoloViz group it is yet another tool to learn for contributors and to maintain for the group. We still **recommend** that you use `pyctdev` to have a development experience that is closer to the one of the core maintainers. If however you feel constrained by the tooling abstraction that is `pyctdev` you can ignore it and reach out to the tools you are most comfortable with. In that case you will have to inspect the files of the project you are contributing to to find what tasks you need to run. In each core HoloViz repository you will find a few files that are of importance for `doit/pyctdev`:

* `dodo.py` is a Python module that allows to add per-project `doit` tasks, refer to [its documentation]() to learn how to add or modify a task. A quick way to identify a task is to find a Python function that is names `task_something`, `doit` makes it then available as a command line subcommand with `doit something`.
* `setup.py` is the classic install file of the [setuptools]() build backend, it is the **single soure of truth of all the dependencies**. In this file you will find:
    * the list of the runtime dependencies required by the package in the `install_requires` key
    * multiple extra dependency groups required to run different tasks in the `extras_require` key, for instance the `doc` extra group would like the dependencies required to build the documentation site
    * in the `extras_require` key you will also find the dependencies required at the *build* time, with for instance `setuptools` declared in that list
* `tox.ini` is the configuration file of [tox]() and where you will find the **configuration of the `doit` commands**. Indeed `pyctdev` creates tasks out of the commands it contains, and uses `tox` directly in some cases (it vendors a version of it).

Now that the main files are defined, we can go through each step of a typical workflow with `pyctdev`, assuming that you are in a cloned repository:

* `conda install -c pyviz/label/dev pyctdev`: to start things off you need to install `pyctdev`, it is available on the `pyviz` channel and we recommend installing a dev release from the dev channel `pyviz/label/dev` to get a more up-to-date version
* `doit env_create -c pyviz -c conda-forge --python=3.8 --name=my_dev_env`: once `pyctdev` is installed you can run the `env_create` command to create a conda environment that will have the Python version and the name you precise, and will fetch packages from the channels you list 
* `conda activate my_dev_env`: to activate the environment you've just created
* `doit -c pyviz -c conda-forge develop_install -o tests -o examples`: the `develop_install` executes three actions, (1) it installs the *build* dependencies (including e.g. `setuptools`), (2) it installs the *runtime* dependencies and the extra dependencies that are listed with the `-o` flag (in the example that would be the *tests* and *examples* groups of dependencies), and (3) it installs the package you're working on in *editable* mode (with `pip install --no-deps --no-build-isolation -e .`).
* `doit test_flakes` (or sometimes `doit test_lint`): run linters on the project code source, e.g. with `flake8`
* `doit test_unit`: run the Python unit tests, i.e. the tests you will find in the `/tests` folder, most likely with `pytest`
* `doit test_examples`: smoke test the  *examples*, i.e. the notebooks you will find in the `/examples` folder

### Documentation

#### nbsite

Most of the packages maitained by the HoloViz group have a website. Only those that are not promoted for usage outside of the group don't, such as `pyctdev`. HoloViz being dedicated to making data visualization simpler in Python, it made sense for the group to come up with a way to generate websites out of a collection of Jupyter Notebooks. As a consequence [nbsite](https://github.com/pyviz-dev/nbsite) was created to achieve that goal. `nbsite` is based on [sphinx](https://www.sphinx-doc.org/en/master/) and is the tool used by all the projects to build their site. `nbsite` provides two important features:

* A Sphinx `NotebookDirective` that allows to insert an evaluated notebook in a document. It has a few useful parameters like `offset` that takes a number that will be the number of top cells not rendered. 
* It can build a gallery from an organised collection of Notebooks.

Building a site with `nbsite` is usually a two-step process:

1. `nbsite generate-rst ...` looks for notebooks in the `examples` folder and generates their corresponding *RestructuredText* files. For instance, if the notebook `examples/user_guide/Data.ipynb` is found, then the corresponding file `doc/user_guide/Data.rst` is created and includes the `NotebookDirective` that points to the notebook file to insert it in this document. A similar process applies for the notebooks found in a gallery.
2. `nbsite build ...` executes the notebooks and builds the website.

After these steps you should find a `builtdocs` folder in the repository that contains the static site built by nbsite/sphinx.

#### File formats

The documentation is currently written in a mix of three file formats:

* *Jupyter Notebooks* (.ipynb): Notebooks are saved in the `examples` folder and are meant to be executed when the documentation is built, which means that the system that builds the documentation must have all the dependencies and data required to run them. Notebooks **must be cleared before being committed** to a repository. TODO: Share somewhere the jq command to clear the notebooks. Thanks to [MyST-NB](https://myst-nb.readthedocs.io/en/latest/), on which `nbsite` depends, *MyST Markdown* is correctly handled in notebooks.
* *reStructuredText* (.rst): Original file format supported by Sphinx and in which the Python documentation is written. They should be gradually replaced by *MyST Markdown* files.
* *Markdown* (.md):  [MyST Markdown](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html#syntax-core) is a Markdown extension focused on scientific and technical documentation authoring. It is easier to write and read compared to *reStructuredText*, and as such should be favored.

#### Theme

The HoloViz sites rely on the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/) for their theme.

#### Analytics

Currenly none of the websites gather any analytics via *Google Analytics*. This used to be the case but this was reverted after the GDPR rules were set (TODO really?).

### Monitoring

#### Status dashboard and scheduled workflows

The [HoloViz Status dashboard](https://status.holoviz.org/) is a static site that allows you to get a quick glance of the status of the packages and repositories maintained by the HoloViz group. It also includes the status of other packages that are important to HoloViz (e.g. Bokeh). The dashboard mostly consists of badges that report various indicators, such as the status of the latest CI test runs, the latest version available on PyPi, whether the documentation is up or not, etc.

Scheduled Github actions have been set up to run on Sundays on most of the packages maintained by the group. This means that checking the *Status Dashboard* on a Monday morning is the right time to get an appreciation of the state of the test/build/docs workflows across the projects.

#### Lumen AE5 Monitor

The [Lumen AE5 Monitor](https://monitor.pyviz.demo.anaconda.com/dashboard) is a dashboard that helps monitoring TODO: what?

### Deployment

S3, AE5

### Testing

pre-commit, linter, nbsmoke (nbval, nbqa), pytest

### Releasing

```{attention}
Releasing a new version of a package is an operation that needs to be done with care, a broken release can adversaly affect many users.
```

```{caution}
Making a new release is not a light operation, it implies many manual steps and has a cost on the general Python ecosystem (e.g. someone needs to update the *conda-forge* release). So make sure that a release is needed before making one, and try not to mess it up too badly ;)
```

### Quick intro

Releasing a new package version is in practice very easy:

1. a commit must be tagged (e.g. `git tag -m "Version 1.9.6 alpha1" v1.9.6a1 master`)
2. that tag must be pushed (e.g. `git push origin v1.9.6a1`)

And that's it, as soon as a new tag is pushed the *Packages* and *Documentation* Github Actions get triggered, start building the packages and the documentation, and deploy them.

```{note}
Version tags must start with a lowercase `v` and have a period in them, e.g. `v2.0`, `v0.9.8` or `v0.1` and may include the [PEP440](https://peps.python.org/pep-0440/) prerelease identifiers of `a` (alpha), `b` (beta) or `rc` (release candidate) allowing tags such as `v2.0.a3`, `v0.9.8.b3` or `v0.1.rc5`.
```

### Distributions

The goal of making a release is to distribute a new package version.

The HoloViz group automatically builds and publishes directly package distributions to two platforms:
* [PyPi](https://pypi.org/): source distribution and wheel
* [Anaconda.org](https://anaconda.org/): conda package

Conda packages are distributed to the [pyviz](https://anaconda.org/pyviz/repo) channel. This allows the HoloViz group to be sure that new packages are available instantaneously to the users as soon as they are published.

The core HoloViz packages are also made available on two other conda channels:

* `defaults`: most of the core HoloViz packages are made available on this channel managed by Anaconda (the company)
* `conda-forge`: the HoloViz members, helped by other contributors, maintain the conda-forge recipes of the packages they publish.

```{note}
Development releases are only available on PyPi and on the conda `pyviz` channel. To install the latest development release of e.g. Panel execute `pip install panel --pre` or `conda install -c pyviz/label/dev panel`.
```

### Before releasing

There are a few tasks that are worth paying attention to before making a release:
* You should have made some decisions about what should go in that release, and check later that these decided changes (bug fixes, new features, documentation, etc.) are indeed merged. This is best managed by setting Github *Milestones* to issues.
* You should make sure that the test suite passes.
* A new release is a good opportunity to check that **there are no alarming warnings** emitted while the tests suite runs. Missing a deprecation warning could mean that you would have to make a new release soon after this one!

### Detailed process

Development releases can have different goals. Sometimes they are only meant to be pre-releases made right before an actual release, to make sure everything is alright. Somtimes they are made to be shared with stakeholders (e.g. a specific contributor, a customer, a dependent project, etc.). Depending on your situation, you might decide to pause the release process in the procedure detailed below between two development releases, waiting for feedback.

1. Before making a proper release, you should start by making a development release. As this is the first one that would be an *alpha* release. Bump the version to e.g. `v1.9.6a1` and commit the new tag.
1. After pushing the new tag you can monitor the *Packages* and *Documentation* workflows. If one of them do not succeed, you will have to fix that as that would be a release blocker.
1. If the *alpha* release succeded, it is now time to check a few things:
    * A new version of the *dev* site should have been built, you should spot check it, trying to find errors that could have occured while the notebooks ran for instance.
    * Some packages have implemented *downstream tests*. When they do, these tests run only when a release is made, they trigger the test suite of their downstream packages (e.g. a Panel release would trigger the test suite of Param). This allows to make sure that the release you just made didn't break some other packages of the HoloViz ecosystem. To find the results of these downstream tests, check the Github Actions page of the released package.
    * Optionally and to make sure that the release went well, you could install the package you've released (e.g. `conda install -c pyviz/label/dev panel`) and check there's no embarassing issue.
1. Pause the release process if you expect feedback from others, if not, keep going.
1. In practice making *beta* releases appear to be quite rare. However making a *release candidate*, in particular before making a release that incorporates breaking changes, is recommended. After making a *release candidate* you should announce it (e.g. on Discourse, Gitter, Twitter) so that users can try it out and provide feedbacks.
1. It is not required to update the changelog for a development release. However, a final release should come with an updated changelog, which means that at some point before making the last development release you will have to merge an updated changelog. Updating the changelog is a process that depends on the package being released, look for files such as `CHANGELOG.md` in the repository and update them accordingly to their format. Crafting a good changelog is an important step in the release process, users will read it carefully to find out what's new and in particular what may potentially break their code. Don't forget to mention all the people who have contributed to the release since the last one.
1. Once the last development release has been confirmed to be in a good shape, by yourself and preferably by others too (in particular when it comes to spot checking the website it is best to have more than one pair of eyes looking into that!), you are ready to make the final release. You will have to bump again the version to its final number (e.g. to `v1.9.6`). Note that you may actually need to make another development release before the final one if you've made some changes after the latest development version that are worth being mentioned in the changelog.
1. Optionally again, and to make sure that the release went well, you could install the package you've released (e.g. `conda install -c pyviz panel`) and check there's no embarassing issue.
1. Create a Github Release, it should contain pretty much the change changelog as the one published on the website (the formatting can change).
1. Find the *conda-forge* recipe of the package you released and update it if required, pay attention in particular to the build and runtime dependencies and their version pins. If you're not yet a maintainer, add yourself in the list of maintainers and ping an existing maintainer, letting them know the PR is ready and that you have added yourself as a maintainer.
1. Announce the release (e.g. on Discourse, Gitter, Twitter).
1. If the release is important (e.g. not a bug fix release), it may be worth a blog post.

```{note}
Bumping the version of a package depends on the package nature:
* Non pure Python packages, e.g. Panel or GeoViews as they invlude JavaScript/TypeScript extensions, need first their `package.json` and `package-lock.json` files to be updated, by manually bumping the version in those files (e.g. from `1.9.5` to `1.9.6-a.1`). Note that the version scheme isn't the same as the Python version scheme.
* Pure Python packages (and non pure Python packages once they've been manually bumped) just need a new tag, this is done as such `git tag -m "Version 1.9.6 alpha1" v1.9.6a1 master`
```

```{note}
Development releases are cheap, don't hesitate to make as many as required! It's also fine if a development release only makes it to one of the two distribution platforms (PyPi or Anaconda.org), they're not meant to be for end-users but for development purposes only.
```

```{tip}
You can tag a release from any branch, not necessarily from the main one. This is useful if you have to maintain multiple versions at the same time (e.g. 2.* and 3.*).
```

```{tip}
If you push a tag by mistake, or the wrong tag, and are lucky enough to spot that right after the fact, you should hurry up (really!) and cancel the *Build* and *Documentation* workflows before anything gets published/deployed. If you manage to do that, you can then remove the faulty tag.
```

### Communication

#### Users

**HoloViz Users** are meant to ask their question on the [HoloViz Discourse forum](https://discourse.holoviz.org/). This Discourse instance is managed by TODO (Philipp?).

### Contributors

**HoloViz Contributors** chat on multiple open channels:

* Directly on Github via issues and pull requests
* On the [PyViz Gitter](https://gitter.im/pyviz/pyviz) which is meant for brainstorming and casual chatting. An example of discussion on Gitter would be when the maintainer of a library that relies on a HoloViz package has in mind a suggestion for an improvement, and requires a first assessment before opening an issue. This Gitter instance is managed by TODO

**HoloViz Contributors** also have regular online meetings, these meetings are **open to anyone**:

* The *HoloViz triaging meeting* takes place every Monday at TODO. Triaging consists of going through the latest opened issues and pull requests, understand them (e.g. that may require to reproduce locally a bug), reply if this was not already done, optionally add a Github label (e.g. `bugs`) and finally but most importantly to assign issues to milestones to prepare for the next releases. You can join the meeting on [Google Meet](meet.google.com/izv-ibmj-cjp) and read the notes on [HackMD](https://hackmd.io/@holoviz/minutes/edit).
* The *HoloViz meeting* takes place every second Friday at TODO. It is a place for coordinating across the HoloViz projects. You can read the notes on [HackMD](https://hackmd.io/@holoviz/minutes/edit). TODO: Right now they're on Zoom, can anyone join?


### Outreach

TODO: Twitter
TODO: Blog (there are actually two blogs!)

### Duties matrix

The HoloViz project has assigned duties to its members...TODO
