# Contributing Guide

This guide includes general guidelines on how to contribute to HoloViz. Read the [Operating Guide](#operating-guide) if you are interested to learn how an Open-Source project like HoloViz operates.

## Contributing? Yes! Wait, but why?

There are many reasons why you would contribute to the HoloViz project, including:

* You appreciate the HoloViz project, its mission and values, and would like to help
* You are a user of one of the HoloViz packages and need a bug to be fixed or a new feature to be implemented, and you are willing to tackle that in some ways
* You are looking for some open-source experience
* You have been reading one of the HoloViz websites and found something to improve, even just a simple typo
* ...

These reasons, or whatever reason brought you here, are all valid to our eyes. We **welcome anyone** who wishes to contribute, and as you will see, there are **many** ways to contribute!

```{hint}
Contributing to the HoloViz project might even get you a job, which has been the case for a couple of HoloViz members.
```

## What and how to contribute?

If you end up on this page it is quite likely that you are interested in contributing code to HoloViz. However, as you will see, there are many other areas where you could contribute, and in some of these areas, the HoloViz project would really appreciate some help!

### Documentation

Each core HoloViz package has its own website. Maintaining the content of these websites is a lot of work, and you can easily help by:

* submitting a PR to fix a typo
* submitting a PR to clarify a section
* submitting a PR to document an undocumented feature
* submitting a PR to update a section that should have been updated
* ...

How the websites look and feel can also be improved. If you happen to have some front-end development expertise, your help would be greatly appreciated.

Finally, the documentation also lies within the code, and in Python, it is found in the so-called *docstrings* that accompany modules, classes, methods and functions. You can easily improve the docstrings by:

* submitting a PR to fix a typo
* submitting a PR to clarify a definition
* submitting a PR to fix or document the default value of a parameter
* ...

```{tip}
Documentation fixes/improvements that are of a small scope usually do not need an issue to be opened beforehand. If you don't have the time to open a pull request, we would appreciate it if you could record your suggestion in an issue on Github. That would already be an excellent contribution!
```

### Support

HoloViz users are recommended to ask their usage questions on the [HoloViz Discourse Forum](https://discourse.holoviz.org/). This forum is only helpful if questions can find answers, and you can be the one writing that answer, which will make somebody else's life so much easier! The HoloViz team members monitor the forum and try to contribute regularly, yet the more we are, the better.

```{tip}
Answering questions on the HoloViz Discourse Forum, or even just trying to answer some random questions, is a very good way to learn how to use the HoloViz tools.
```

Some users also ask questions on [StackOverflow](https://stackoverflow.com/), which isn't much monitored by the HoloViz team, so we would greatly appreciate any help there. 

### Outreach

Before addressing how to contribute code to HoloViz, it is important to mention that a beneficial way to contribute to HoloViz is by communicating more about it. Tweeting, writing blog posts, creating Youtube videos, presenting your work with one or more of the HoloViz tools, etc., are all outreach activities that serve the purpose of HoloViz.

### Code

Contributing code includes:

* fixing an existing bug: the recommended practice is to add one or more unit test(s) that would have failed before the bug fix was implemented.
* adding a new feature: again, the recommended practice is to add unit test(s) to test the new feature's functionality.
* improving performance: while slow code isn't necessarily a bug, users always appreciate faster code. Performance improvements should be demonstrated by some benchmark comparing the performance before and after the changes.
* adding tests: test coverage can always be improved. Adding tests is a good way for beginners to contribute to a project and familiarize themselves with its code base and workflows.
* refactoring: refactoring can be a good way to improve a code base.

### Developer Instructions


```{note}
The HoloViz projects usually provide specific instructions to set up your environment to be ready to contribute documentation or code to the project. The instructions provided hereafter are meant to be general enough to apply to each project. Refer to the documentation of the project you are working on for more details.
```

Before making anything beyond a minimal contribution (e.g. fixing a type), the first step is usually to open a [GitHub Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) that documents what you are trying to fix/improve. Writing a good issue is important and will affect how it is going to be perceived by the project maintainers, contributors and watchers. Read for instance this [blog post](https://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports) that describes what a good issue should look like.  Once an issue is opened, a discussion can take place with the maintainers to see if what is suggested is relevant, which can orientate the action to take.

The first step to working on any source code is to install Git as the source codes are stored in [Git](https://git-scm.com) source control repositories. To install Git on any platform, refer to the [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) section of the [Pro Git Book](https://git-scm.com/book/en/v2).

As an external contributor, you do not have permission to submit code directly to any of the repositories. Github offers you to fork the repository, which will create a copy of the repository, on which you will have the right to work freely. Follow [these instructions](https://docs.github.com/en/get-started/quickstart/fork-a-repo) to find out how to fork and clone a repository.

The HoloViz developers rely on [Conda](https://conda.io/docs/intro.html) to manage their virtual environments. We **recommend** you install Conda too to have an experience as close as possible to those of the core developers. To install Conda on any platform, you can [install Miniconda](https://docs.conda.io/en/latest/miniconda.html). 

The HoloViz developers rely on [pyctdev](https://github.com/pyviz-dev/pyctdev), a custom developer tool that facilitates maintaining all of the holoviz projects. pyctdev is an extension of the task running tool [doit](https://pydoit.org/). We **recommend** that you install `pyctdev`:

```bash
conda install -c pyviz/label/dev "pyctdev>0.5.0"
```

Once `pyctdev` is available and you are in the cloned (e.g. panel) repository, you can create a new virtual environment with the `env_create` *doit* command with the appropriate channels:

```bash
doit env_create -c channel1 -c channel2 --name=dev-env --python=3.x
```

Don't forget to activate this environment:

```bash
conda activate dev-env
```

To perform an editable install of the project you are working on, including all the dependencies required to run the full unit test suite, run the `develop_install` with the appropriate channels and options:

```bash
doit develop_install -c channel1 -c channel2 -o tests -o ... -o ...
```

For example:

```bash
doit develop_install -c pyviz/label/dev -c conda-forge -o tests -o examples
```

Depending on the options you have chosen to install (usually `-o tests` for the unit tests, `-o examples` to run the examples notebooks, ...), the following commands will run:

* The unit tests: `doit test_unit.`
* The examples tests: `doit test_examples.`

```{warning}
The *options* and *commands* are not standardized across the HoloViz projects. Refer to the project documentation for the exact commands to run.
```

```{hint}
The reference sources to find out which commands to run to install the correct dependencies and to execute the tests and other tasks are the **Github Actions Workflows** files that you can find in the `.github` folder of each repository. 
```

At this step, you should have your environment set up, being able to run tests and a clone of the source repository. The next step is to create a branch and start making changes. Before committing these changes, make sure the tests still pass by running them. The HoloViz source codes are stringent concerning styling (e.g., they're not using [black](https://github.com/psf/black)). Try to write code that follows the style of the surrounding code. Once you are done with your changes, you can commit them. It is good practice to break down big changes into smaller chunks, and each chunk has its own commit with a message that summarizes it. Now you can push the branch to your clone and create a *pull request* from your clone to the original repository. This [Github Gist](https://gist.github.com/Chaser324/ce0505fbed06b947d962) describes these GitHub steps in more detail.

The *pull request* you make should reference the *issue* you are attempting to close (i.e. `Fixes #issuenumber`) and include a description of the changes you made. Changes affecting the visual properties should include screenshots or GIFs.

Your *pull request* should now be reviewed by one of the project's maintainers. This may take a while given how busy the maintainers are, so try to be patient :). Your pull request will be evaluated to ensure that it is within the scope of the project (again, it's a good idea to create an issue first to outline your intent and give the maintainers an opportunity to weigh in before you spend the effort creating a pull request). If it's decided to proceed, the review will be conducted, and once the review is done you may be required to make some changes. You may also be asked to *resolve conflicts* if the changes you made appear to conflict with changes made to the source code after you submitted the *pull request*.

When your PR is merged, enjoy, and repeat!

## Operating guide

The HoloViz project consists of:

* Several core packages (including Panel, Lumen, HoloViews, GeoViews, Datashader, hvPlot, Colorcet, and Param) that must be maintained, tested, documented, etc.
* A group of people collaborating to make the project better.

This section of the guide describes how that system works.


### PyViz

The HoloViz project was previously named *PyViz* but the Python community suggested that it wasn't that appropriate and as such *PyViz* was renamed *HoloViz*, inspired by HoloViews. As renaming is a lot of work and can potentially break some systems, you will still find references to PyViz here and there. Notably, in the installation guide of each HoloViz package where the recommended installation command with conda is `conda install -c pyviz package`.

*PyViz*, or [PyViz.org](https://pyviz.org/), is now a community project of its own. It is a fully open guide to all Python visualization tools. The HoloViz group maintains the [pyviz](https://github.com/pyviz) organization, but only for historical reasons, as it is meant to be shared by the whole Python visualization community.

### GitHub/Git

#### Organisations and repositories

HoloViz consists of several Python projects. All these projects are version-controlled with [Git](https://git-scm.com/) and hosted on GitHub. Having all the projects hosted on GitHub means that HoloViz can rely on all the excellent features Github freely provides to open-source projects, including easy collaboration through *Issues and Pull Requests (PR)*, continuous integration (CI) with *GitHub Actions (GHA)* and documentation hosting with *GitHub Pages*.

```{warning}
It is crucial to keep in mind that nothing lasts forever and that, at some point, HoloViz may be forced to rely on other platforms or services. The more HoloViz relies on GitHub, the more difficult any transition to another system is.
```

The HoloViz group owns a few GitHub organizations:

* [holoviz](https://github.com/holoviz/) is the main one where you are likely to contribute. It hosts the core packages maintained by the group.
* [pyviz-dev](https://github.com/pyviz-dev/) hosts two main types of repositories:
    * Packages that support maintaining the core HoloViz packages, including, for instance, `nbsite`, `nbsmoke`, `pyctdev`, `pyct` and `autover`. These support packages were developed when no alternative, or satisfying alternative, was available at the time the group needed them.
    * Repositories that are only used to host *dev* builds of the core packages websites, i.e., no actual work is done on these repositories. They just get updated automatically in a CI process. 
* [holoviz-topics](https://github.com/holoviz-topics/) hosts repositories that demonstrate concrete usage of the HoloViz tools.
* [holoviz-demos](https://github.com/holoviz-demos/) hosts some demos, mostly Panel apps. It is meant to be removed.
* [holoviz-community](https://github.com/holoviz-community/) is a place for the HoloViz community to host repositories that are going to be nicely exposed under the HoloViz umbrella

In more detail:

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
* [holoviz-topics](https://github.com/holoviz-topics/)
    * [examples](https://github.com/holoviz-topics/examples): Home for domain-specific narrative examples using multiple PyViz projects
    * [earthsim](https://github.com/holoviz-topics/earthsim): Project for developing Python-based workflows for specifying, launching, visualizing, and analyzing environmental simulations
    * [earthml](https://github.com/holoviz-topics/earthml): Machine learning and visualization in Python for Earth science
    * [holodoodler](https://github.com/holoviz-topics/holodoodler): Python application that allows interactive construction of sparse labeling for image segmentation using deep neural networks
    * more ...

#### Teams

The `holoviz` organization has two teams:

* `holoviz-dev`: Team that will manage the HoloViz contents
* `Triaging team`: Contributors able to triage open issues on HoloViz projects

The `pyviz-dev` organization has one team:

* `pyviz-dev`: PyViz Developers

The `holoviz-topics` organization has one team:

* `pyviz-dev`: Developers on HoloViz Topics

#### Developer account

* [HoloViz Developers](https://github.com/holoviz-developers): Account to use for automated actions on HoloViz projects
* [PyViz Developers](https://github.com/pyviz-developers)

#### Repository structure

The core packages have their repository that, except in a few cases, all share the same structure:

* The tests are nested under the package directory, e.g., at `panel/tests`. The tests are then automatically bundled in the source distribution, which makes it a little easier for repackagers to run the tests.
* The `examples` and the `doc` folder share the same structure, e.g. you will find `panel/doc/user_guide`  and `panel/examples/user_guide`. The `examples` folder contains Jupyter Notebooks, while the `doc` folder usually contains *reStructuredText* and *Markdown* files. The HoloViz packages generally have `pyct` as a build dependency, which can be used to add an `examples` command to a project (e.g. `panel examples`) to make it easier for users to download the project notebooks. The `examples` folder is bundled within the package source, so users running `panel examples` get the notebooks copied from the package to a local directory. The `doc` folder isn't bundled within the package source.
* The `.github` directory contains GitHub specific configuration files, e.g., for GitHub Actions.
* Optional: the `conda.recipe` directory contains a conda recipe template used by the building tooling when creating a conda package.
* Optional: the `binder` directory contains configuration files to setup [binder](https://mybinder.org/)


#### Git workflow

The HoloViz projects follow the standard Github workflow:

* An *issue* should be created before submitting a *pull request* (PR) unless the scope of the planned PR is minimal, such as fixing a typo.
* *Pull requests* must be based on the main (e.g., *main*) branch and kept up to date with this branch. Merging the main branch onto the working branch is recommended instead of rebasing, particularly if you are not working alone on that branch.
* *Pull requests* must be reviewed before being merged. Each project has one or more reviewer(s) assigned.
* The commits of a *Pull request* are automatically [squashed on merge](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github#squashing-your-merge-commits). This means that you don't have to particularly well craft your commit messages in your branch as they won't be part of the main git history.

### Tooling

#### Conda

The HoloViz group relies heavily on the [conda package manager](https://conda.io/docs/intro.html) for the following reasons:

* The HoloViz group consists of people who have a scientific background. Installing the Python scientific libraries was at some point a complicated task to achieve with `pip` as these libraries usually depend on binary dependencies that need to be compiled, a step that pip delegates to whatever tool is installed on your machine. `conda` was created to solve this exact problem and the HoloViz group was an early user of this solution. While it's important to note that installing scientific libraries with `pip` has become a smoother experience (notably because more wheels are being distributed), installing some packages like those of the Python geo-stack (`rasterio`, `pyproj`, etc.) still proves to be challenging, and `conda` *usually* provides a better experience.
* The core maintainers of the HoloViz group are employed by [Anaconda](https://www.anaconda.com/), and as such, it makes sense for the group to use `conda`
* Some HoloViz-maintained packages such as `Panel` require software like `node.js`, which `pip` cannot install. In contrast, they can be installed with `conda`. `conda` allows to create a complete dev environment without having to install other software from another way, e.g., with `brew` on macOS.

To contribute to HoloViz, we **recommend** that you use `conda`. You would have a closer experience with the maintainers, and they will be in a better position to help you set up your dev environment and debug whatever issue you may encounter.

To install Conda on any platform, see the [Download conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html) section of the [conda documentation](https://conda.io/docs/index.html).

Of course, this is not a strict requirement, and you can decide to use `pip` instead!

#### Pyctdev

[pyctdev](https://github.com/pyviz-dev/pyctdev) stands for *python packaging common tasks for developers*, it is a developer tool built by the HoloViz group in an attempt to simplify managing Python projects, by providing a way to declare how to run the usual tasks required to maintain a project, such as running its unit tests or building its documentation, and by standardizing the way to execute these tasks with e.g. `doit test_unit` or `doit build_website`. `pyctdev` relies on [doit](https://pydoit.org/) to provide a command-line interface to developers (e.g. `doit test_unit`) and can be as such seen as an extension of `doit`. `doit` allows to register *tasks* that consist of a sequence of *actions*, an action being either a command line instruction (e.g. `flake8 .`) or the execution of a Python function. `pyctdev` comes with various common Python tasks dedicated to manage a project, such as the `develop_install` task (executed with `doit develop_install`) that will install the project in development mode with its optional development dependencies.

By unifying the way to execute these common tasks, `pyctdev` makes it easier to work across the HoloViz projects. It also makes it easier to work across environments, as the commands to execute should be the same whether you execute them locally or in a CI environment. In addition, `pyctdev` supports developing with either pip or conda, a unique feature. In practice, however, `pyctdev` is an ambitious project. While it has proven useful to the HoloViz group, it is yet another tool to learn for contributors and maintain for the group. We still **recommend** that you use `pyctdev` to have a development experience closer to the core maintainers. If you feel constrained by the tooling abstraction that is `pyctdev,` you can ignore it and reach out to the tools you are most comfortable with. In that case, you will have to inspect the files of the project you are contributing to and find what tasks you need to run. In each core HoloViz repository, you will find a few files that are of importance for `doit/pyctdev`:

* `dodo.py` is a Python module that allows adding per-project `doit` tasks. Refer to [its documentation](https://pydoit.org/contents.html) to learn how to add or modify a task. A quick way to identify a task is to find a Python function named `task_something`, `doit` makes it available as a command line subcommand with `doit something`.
* `setup.py` is the classic install file of the [setuptools](https://setuptools.pypa.io) build backend. It is the **single source of truth of all the dependencies**. In this file, you will find:
    * the list of the runtime dependencies required by the package in the `install_requires` key.
    * multiple extra dependency groups are required to run different tasks in the `extras_require` key. For instance, the `doc` extra group would like the dependencies required to build the documentation site.
    * in the `extras_require` key, you will also find the dependencies required at the *build* time like `setuptools`.
* `tox.ini` is the configuration file of [tox](https://tox.wiki) and where you will find the **configuration of the `doit` commands**. Indeed `pyctdev` creates tasks out of the commands it contains and uses `tox` directly in some cases (it vendors a version of it).

Now that the main files are defined, we can go through each step of a typical workflow with `pyctdev`, assuming that you are in a cloned repository:

* `conda install -c pyviz/label/dev pyctdev`: to start things off, you need to install `pyctdev`. It is available on the `pyviz` channel, and we recommend installing a dev release from the dev channel `pyviz/label/dev` to get a more up-to-date version
* `doit env_create -c pyviz -c conda-forge --python=3.8 --name=my_dev_env`: once `pyctdev` is installed, you can run the `env_create` command to create a conda environment that will have the Python version and the name you want, and will fetch packages from the channels you have listed.
* `conda activate my_dev_env`: to activate the environment you've just created.
* `doit -c pyviz -c conda-forge develop_install -o tests -o examples`: the `develop_install` executes three actions, (1) it installs the *build* dependencies (including, e.g., `setuptools`), (2) it installs the *runtime* dependencies and the extra dependencies that are listed with the `-o` flag (in the example that would be the *tests* and *examples* groups of dependencies), and (3) it installs the package you're working on in *editable* mode (with `pip install --no-deps --no-build-isolation -e .`).
* `doit test_flakes` (or sometimes `doit test_lint`): run linting on the project code source, e.g., with `flake8`.
* `doit test_unit`: run the Python unit tests, i.e., the tests you will find in the `/tests` folder, most likely with `pytest`.
* `doit test_examples`: smoke test the  *examples*, i.e., the notebooks you will find in the `/examples` folder.

### Documentation

#### nbsite

Most of the packages maintained by the HoloViz group have a website. Those not promoted for usage outside the group don't have a website like `pyctdev`. HoloViz being dedicated to making data visualization simpler in Python, it made sense for the group to develop a way to generate websites out of a collection of Jupyter Notebooks. As a result, [nbsite](https://github.com/pyviz-dev/nbsite) was created to achieve that goal. `nbsite` is based on [sphinx](https://www.sphinx-doc.org) and is the tool used by all the projects to build their site. `nbsite` provides two important features:

* A Sphinx `NotebookDirective` allows inserting an evaluated notebook in a document. It has a few useful parameters like `offset` that takes a number that will be the number of top cells not rendered. 
* It can build a gallery from an organized collection of Notebooks.

Building a site with `nbsite` is usually a two-step process:

1. `nbsite generate-rst ...` looks for notebooks in the `examples` folder and generates their corresponding *reStructuredText* files. For instance, if the notebook `examples/user_guide/Data.ipynb` is found, then the corresponding file `doc/user_guide/Data.rst` is created and includes the `NotebookDirective` that points to the notebook file to insert it in this document. A similar process applies to the notebooks found in a gallery.
2. `nbsite build ...` executes the notebooks and builds the website.

After these steps, you should find a `builtdocs` folder in the repository that contains the static site built by nbsite/sphinx. When the websites are built in the continuous integration system, the content of the `builtdocs` folder is pushed to a `gh-pages` branch. The details of this process can be found in the `docs.yaml` Github Action workflow of each project, located in the `.github/workflows` folder.

#### File formats

The documentation is currently written in a mix of three file formats:

* *Jupyter Notebooks* (.ipynb): Notebooks are saved in the `examples` folder and are meant to be executed when the documentation is built, which means that the system that builds the documentation must have all the dependencies and data required to run them. Notebooks **must be cleared before being committed** to a repository. The team uses a [custom shell script](https://gist.github.com/maximlt/a9fa4d19ae5bff83422194ca99533faa) that leverages `jq` to strip out some data and metadata from the notebook JSON file. Thanks to [MyST-NB](https://myst-nb.readthedocs.io/en/latest/), on which `nbsite` depends, *MyST Markdown* is correctly handled in notebooks.
* *reStructuredText* (.rst): Original file format supported by Sphinx and in which the Python documentation is written. They should be gradually replaced by *MyST Markdown* files.
* *Markdown* (.md):  [MyST Markdown](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html#syntax-core) is a Markdown extension focused on scientific and technical documentation authoring. It is easier to write and read compared to *reStructuredText*, which should be favored.

#### Theme

The HoloViz sites rely on the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/) for their theme.

#### Analytics

Currently, most of the websites gather analytics via *Google Analytics*.

#### Hosts

The HoloViz websites are usually hosted on *GitHub Pages*. The deployment process involves pushing the website built to the `gh-pages` branch, which is watched by GitHub and will trigger a site update on change. This process is based on Git and comes with some size limitations, which means that it wasn't possible to deploy HoloViews' website this way, which is instead hosted on AWS S3.

#### Dev sites

Most HoloViz projects have both the main site - the one meant to be visited by users and that is in line with the latest official release - and a dev site that can be updated at any time and is meant to be used by the HoloViz developers for testing purposes, and in particular making sure that the documentation build works as expected before making a new release.

This page references all the HoloViz dev sites: https://pyviz-dev.github.io/. A link to the dev site is also usually available in the README file of each project.

### Monitoring

#### Status dashboard and scheduled workflows

The [HoloViz Status dashboard](https://status.holoviz.org/) is a site that lets you glance at the status of the packages and repositories maintained by the HoloViz group. It also includes the status of other packages important to HoloViz, e.g., Bokeh. The dashboard primarily consists of badges that report various indicators, such as the status of the latest CI test runs, the latest version available on PyPi, whether the documentation is up or not, etc.

Scheduled Github actions have been set up to run on Sundays on most of the packages maintained by the group. This means that checking the *Status Dashboard* on a Monday morning is the right time to get an appreciation of the state of the test/build/docs workflows across the projects.

#### Lumen AE5 Monitor

The [Lumen AE5 Monitor](https://monitor.pyviz.demo.anaconda.com/dashboard) is a dashboard that helps monitor the state and performance of the deployments.

#### Deployments

All the HoloViz websites are static websites. Yet many of their pages would actually require an active Python kernel to be fully interactive. I.e., any datashader examples on HoloViews' website would require a kernel to show users that data shading is done every time their plot changes. Some websites have implemented deployments to show users how the tools behave in a fully interactive environment. As the core HoloViz members are employed by Anaconda, they have access to an Anaconda product named [Enterprise Data Science Platform](https://www.anaconda.com/products/enterprise) (also called *AE5*) that is a platform to, among other things, allow to easily develop and deploy projects, like for instance Jupyter Notebooks or Panel apps. The HoloViz group has set up an AE5 instance and used it to deploy applications for the following websites:

* [Panel](https://panel.holoviz.org/): the *Gallery* applications are deployed this way. They are then iframed on Panel's site.
* [Examples](https://examples.pyviz.org/): this site offers users to run read-only Jupyter Notebooks and web apps like Panel apps (look for *View a running version of this notebook.* in the example header).


#### Data Storage

It is sometimes convenient to have a place where to store data. This happens when the data is too large to be stored on a GitHub repository (storing data there isn't recommended anyway), which is pretty standard when creating a tutorial that relies on an actual data set. The HoloViz group makes use of the following AWS S3 buckets:

* datashader-data
* TODO

These buckets are managed by @jlstevens and @philippjfr.

#### Domain names

Some of the sites have their own domain name:

* datashader.org
* holoviews.org
* geoviews.org

While others are available as subdomains of holoviz.org:

* hvplot.holoviz.org
* panel.holoviz.org
* lumen.holoviz.org
* param.holoviz.org
* colorcet.holoviz.org

### Testing

While `pyctdev` acts as the task runner, other tools run the tests. There are four main kinds of tests that a HoloViz project may run:

* *Linters*: running programs that check Python source files for errors and styling issues. Most HoloViz projects rely on [Flake8](https://flake8.pycqa.org) and use the `doit test_flakes` command. Some projects may rely on [pre-commit](https://pre-commit.com/) to run the linters on every commit to avoid having the CI fail in linting issues, which are best found locally. Notebooks can also be linted, this is done either by [nbsmoke](https://github.com/pyviz-dev/nbsmoke) or [nbqa](https://nbqa.readthedocs.io/).
* *Unit tests*: the HoloViz projects rely on [pytest](https://docs.pytest.org/) to run their unit tests, sometimes with some additional pytest plugins. [pytest-cov](https://pytest-cov.readthedocs.io/) usage is pretty standard across the projects, as it provides an easy way to produce coverage reports that can then automatically be uploaded to the [Codecov](https://about.codecov.io/) service. The `doit test_unit` command is usually the one that will run these tests.
* *Example tests*: the examples tests and the notebooks tests, in which the notebooks found in the `/examples` folder are all executed. Note that their output is not compared with any reference. Instead, the tests only fail if an error is raised while running the notebooks. The projects rely on pytest and either [nbsmoke](https://github.com/pyviz-dev/nbsmoke) or [nbval](https://nbval.readthedocs.io). The `doit test_examples` command is usually the one that will run these tests.
* *UI tests*: some projects may rely on [Playwright](https://playwright.dev/python/) and [pytest-playwright](https://github.com/microsoft/playwright-pytest) to run tests that check that things get displayed as expected in a browser and those interactions between the client and the backend work as expected. The `doit test_ui` command is usually the one that will run these tests.

```{note}
We would like not to have to maintain nbsmoke anymore and instead rely on nbqa and nbval.
```

### Releasing

```{attention}
Releasing a new version of a package is an operation that needs to be done with care, a broken release can adversely affect many users.
```

```{caution}
Making a new release is a cumbersome and delicate operation. It implies many manual steps and has a cost on the general Python ecosystem, e.g., someone needs to update the *conda-forge* release). So make sure that a release is needed before making one, and try not to mess it up too badly ;)
```

#### Quick intro

Releasing a new package version is, in practice, very easy:

1. a commit must be tagged (e.g. `git tag -m "Version 1.9.6 alpha1" v1.9.6a1 main`)
2. that tag must be pushed (e.g. `git push origin v1.9.6a1`)

And that's it, as soon as a new tag is pushed, the *Packages* and *Documentation* Github Actions get triggered, and start building the packages and the documentation, and deploy them.

```{note}
Version tags must start with a lowercase `v` and have a period in them, e.g. `v2.0`, `v0.9.8` or `v0.1` and may include the [PEP440](https://peps.python.org/pep-0440/) prerelease identifiers of `a` (alpha), `b` (beta) or `rc` (release candidate) allowing tags such as `v2.0.a3`, `v0.9.8.b3` or `v0.1.rc5`.
```

#### Distributions

The goal of making a release is to distribute a new package version.

The HoloViz group automatically builds and publishes package distributions directly to two platforms:
* [PyPi](https://pypi.org/): source distribution and wheel
* [Anaconda.org](https://anaconda.org/): conda package

Conda packages are distributed to the [pyviz](https://anaconda.org/pyviz/repo) channel. This allows the HoloViz group to be sure that new packages are available instantaneously to the users as soon as they are published.

The core HoloViz packages are also made available on two other conda channels:

* `defaults`: most of the core HoloViz packages are made available on this channel managed by Anaconda (the company)
* `conda-forge`: the HoloViz members, helped by other contributors, maintain the conda-forge recipes of the packages they publish.

```{note}
Development releases are only available on PyPi and the conda `pyviz` channel. To install the latest development release, e.g., Panel execute `pip install panel --pre` or `conda install -c pyviz/label/dev panel`.
```

#### Before releasing

There are a few tasks that are worth paying attention to before making a release:
* You should have made some decisions about what should go in that release and check later that these decided changes (bug fixes, new features, documentation, etc.) are indeed merged. This is best managed by setting Github *Milestones* to issues.
* You should make sure that the test suite passes.
* A new release is a good opportunity to check that **there are no alarming warnings** emitted while the tests suite runs. Missing a deprecation warning could mean that you would have to make a new release soon after this one!

#### Detailed process

Development releases can have different goals. Sometimes they are only meant to be pre-releases made right before an actual release to make sure everything is alright. Sometimes they are made to be shared with stakeholders (e.g., a specific contributor, a customer, a dependent project, etc.). Depending on your situation, you might decide to pause the release process in the procedure detailed below between two development releases, waiting for feedback.

1. Before making a proper release, you should start by making a development release. This is the first one that would be an *alpha* release. Bump the version too, e.g., `v1.9.6a1` and commit the new tag.
1. After pushing the new tag, you can monitor the *Packages* and *Documentation* workflows. If one fails, you will have to fix that as that would be a release blocker.
1. If the *alpha* release succeeded, it is now time to check a few things:
    * A new version of the *dev* (built on the corresponding `pyviz-dev` repository `gh-pages` branch) site should have been built. You should spot-check it, trying to find errors that could have occurred while the notebooks ran, for instance.
    * Some packages have implemented *downstream tests*. When they do, these tests run only when a release is made. They trigger the test suite of their downstream packages (e.g., a Panel release would trigger the test suite of Param). This ensures that the release you just made didn't break some other packages of the HoloViz ecosystem. To find the results of these downstream tests, check the Github Actions page of the released package.
    * Optionally, and to make sure that the release went well, you could install the package you've released (e.g. `conda install -c pyviz/label/dev panel`) and check there's no embarrassing issue.
1. Pause the release process if you expect feedback from others. If not, keep going.
1. In practice making *beta* releases appear to be quite rare. However, making a *release candidate*, in particular before making a release that incorporates breaking changes, is recommended. After making a *release candidate* you should announce it (e.g., on Discourse, Gitter, Twitter) so that users can try it out and provide feedback.
1. It is not required to update the changelog for a development release. However, a final release should come with an updated changelog, which means that at some point before making the last development release, you will have to merge an updated changelog. Updating the changelog is a process that depends on the package being released. Look for files such as `CHANGELOG.md` in the repository and update them accordingly to their format. Crafting a good changelog is an important step in the release process. Users will read it to find out what's new and, in particular, what may potentially break their code. Don't forget to mention all the people who have contributed to the release since the last one.
1. Once the last development release has been confirmed to be in good shape, by yourself and preferably by others too (in particular, when it comes to spot-checking the website, it is best to have more than one pair of eyes looking into that!), you are ready to make the final release. You will have to bump the version again to its final number (e.g., to `v1.9.6`). Note that you may need to make another development release before the final one if you've made changes after the latest development version that are worth mentioning in the changelog.
1. Optionally again, and to ensure the release went well, you could install the package you've released (e.g. `conda install -c pyviz panel`) and check there's no embarrassing issue.
1. Create a Github Release. It should contain the same changelog as the one published on the website (the formatting can change).
    * Go to the Github repository
    * Click *Releases*
    * Click *Tags*
    * Click the most recent tag that you just added 
    * Click *Create a new release*
    * Add release notes and publish the release 
1. Find the *conda-forge* recipe of the package you released and update it if required. Pay attention to the build and runtime dependencies and their version pins. If you're not yet a maintainer, add yourself to the list of maintainers and ping an existing maintainer, letting them know the PR is ready and that you have added yourself as a maintainer.
1. Announce the release (e.g., on Discourse, Gitter, Twitter).
1. If the release is important (e.g., not a bug fix release), it may be worth a blog post.

```{note}
Bumping the version of a package depends on the package's nature:
* Non-pure Python packages, e.g., Panel or GeoViews as they include JavaScript/TypeScript extensions, need their `package.json` and `package-lock.json` files to be updated, manually bumping the version in those files (e.g., from `1.9.5` to `1.9.6-a.1`). Note that the version scheme isn't the same as the Python version scheme.
* Pure Python packages (and non-pure Python packages once manually bumped) just need a new tag, done with `git tag -m "Version 1.9.6 alpha1" v1.9.6a1 main`.
```

```{note}
Development releases are cheap, don't hesitate to make as many as required! It's also fine if a development release only makes it to one of the two distribution platforms (PyPi or Anaconda.org). They're not meant to be for end-users but development purposes only.
```

```{tip}
You can tag a release from any branch, not necessarily from the main one. This is useful if you have to maintain multiple versions simultaneously (e.g., 2.* and 3.*).
```

```{tip}
If you push a tag by mistake or the wrong tag and are lucky enough to spot that instantly, you should hurry up (really!) and [cancel](https://docs.github.com/en/actions/managing-workflow-runs/canceling-a-workflow) the *Build* and *Documentation* workflows before anything gets published/deployed. If you manage to do that, you can then remove the faulty tag.
```

### Communication

#### Users

**HoloViz Users** are meant to ask their questions on the [HoloViz Discourse forum](https://discourse.holoviz.org/). This Discourse instance is managed by @philippjfr.

#### Contributors

**HoloViz Contributors** chat on multiple open channels:

* Directly on Github via issues and pull requests
* On the [PyViz Gitter](https://gitter.im/pyviz/pyviz), which is meant for brainstorming and casual chatting. An example of a discussion on Gitter would be when the maintainer of a library that relies on a HoloViz package has in mind a suggestion for an improvement and requires a first assessment before opening an issue.

**HoloViz Contributors** also have regular online meetings. These meetings are **open to anyone**. Please see the [Community](https://holoviz.org/community.html) page for a calendar and description of the meetings.

#### Outreach

##### Blogs

The HoloViz project maintains a blog at https://blog.holoviz.org/ where new major releases are announced.

The former PyViz-named blog is still alive at http://blog.pyviz.org/.

##### Twitter

There are four more or less active Twitter accounts:

* [@Holoviz_org](https://twitter.com/holoviz_org)
* [@Panel_org](https://twitter.com/panel_org)
* [@Datashader](https://twitter.com/datashader)
* [@HoloViews](https://twitter.com/HoloViews)
