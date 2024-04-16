# HEP 2: Release and deprecation policies

<table>
<tr><td> Identifier </td><td> HEP 2 </td>
<tr><td> Title </td><td> Release and deprecation policies </td>
<tr><td> Status </td><td> Draft </td></tr>
<tr><td> Author(s) </td><td> Maxime Liquet </td></tr>
<tr><td> Created </td><td> TBD </td></tr>
<tr><td> Updated </td><td> - </td></tr>
<tr><td> Discussion </td><td> https://github.com/holoviz/holoviz/pull/388 </td></tr>
<tr><td> Implementation </td><td> NA </td></tr>
</table>

## Summary

This HEP outlines unified release and deprecation policies for the HoloViz Projects. It addresses key questions about the lifecycle of features, including deprecation and removal timelines. The HEP formalizes existing release procedures and introduces well-defined deprecation guidelines to streamline long-term maintenance and decision-making processes, aiming for consistency across projects and an improved user experience.

## Motivation

The Projects already follow a pretty consistent procedure when it comes to releases, which this HEP formalizes. However, the Projects have applied various approaches for their deprecation cycle, and without clear guidelines this has sometimes led to long and unproductive discussions. The HEP aims to improve this by introducing new and well defined guidelines. Making it easier for Projects to deprecate features is **key to their long-term maintenance**.

Indeed, the goal of deprecating a feature is often to reduce the long-term maintenance burden of a Project. However, the act itself of deprecating a feature - the deprecation cycle - is a process that requires many actions be undertaken by the maintainers of a Project, starting from when they begin discussing the deprecation to when they remove the deprecated feature, which will potentially be done by other maintainers multiple years later. Given the complexity of the process and its somewhat remote benefits, without clear guidelines it's easy for maintainers to make mistakes, potentially affecting the user experience.

At the time of writing this HEP the Projects do not have a clear plan for their deprecation cycle. They also often adopt non-standard practices. For instance, many Projects display deprecation warnings using the logging API provided by Param (`param.main.param.warning(...)`), while in the Python ecosystem it is much more common to use the function `warnings.warn` from the standard library. With this function, users can easily control the behavior of these warnings (e.g. hide them, turn them into errors).

The overall goal of the HEP is to ensure that these policies are **consistently applied across the Projects**, which will help provide a **consistent user experience** and **help contributors and maintainers make decisions**. We also aim to adopt **standard practices**.

## Specification

### Release policy

#### Versioning

The Projects deliver final releases with a version number of the form `<major>.<minor>.<patch>` (e.g. `1.2.3`):

- `patch` releases (e.g. 0.1.**0** -> 0.1.**1**) should never intentionally and rarely, if ever, unintentionally break API. Should be safe to upgrade to the latest patch release if you encounter any problems.
- `minor` releases (e.g. 0.**1**.1 -> 0.**2**.0) should not have API changes that affect most users. API changes in minor releases should be rare, but are not unheard of, particularly for recently added functionality whose API is still being refined, or for bugs found in older code that can't be fixed without changing API at least slightly.
- `major` releases (e.g. **0**.2.0 -> **1**.0.0)  will typically break APIs, but should normally include significant new functionality to motivate users to update their code. Major breaking API changes should be postponed to a major release and paired with significant user-visible advantages.

While this versioning scheme is inspired by [Semantic Versioning](https://semver.org/) (*SemVer*), like many other Python projects, **the HoloViz Projects do not strictly follow it** as incompatible (aka breaking) API changes are not limited to `major` releases.

The Projects can deliver three types of pre-releases / development versions:

- `alpha` (e.g. `1.2.3a1`): Projects can deliver alpha releases for users to benefit from and/or test bug fixes and new features, early in the development phase of a new version. alpha releases are common across the Projects.
- `beta` (e.g. `1.2.3b1`): Projects can deliver beta releases for the same reasons, except they indicate the project is in a more advanced development phase of a new version. beta releases are not common across the Projects, they're more likely to be useful when a major release is in development, to progressively deliver large new features and API breaking changes.
- `release candidate` (e.g. `1.2.3rc1`): Projects must deliver at least one release candidate version before the final release and Projects should not add new features between release candidates. There is no expectation from Projects to announce their release candidates to a wide audience and wait some time before making a final release. However, Projects are encouraged to adopt that approach when they prepare an important release, typically a major or a significant minor release.

#### Supported versions

Aside from certain exceptional cases, the Projects are not expected to backport changes to previous major or minor releases.

#### Distribution

HoloViz release managers are responsible for distributing the Projects on these platforms:

- Pre-releases are distributed on [PyPI](https://pypi.org) and on the *pyviz/label/dev* channel of [Anaconda.org](https://anaconda.org).
- Final versions are distributed on [PyPI](https://pypi.org), and on the  *conda-forge* and *pyviz* channels of [Anaconda.org](https://anaconda.org).

#### Release cadence

The Projects have not adopted a regular release cadence; a new release happens whenever maintainers find it is appropriate. A Project is free to adopt a regular release cadence.

Major regressions in a release should be fixed and released in a new patch version as soon as possible.

### Backwards compatibility

The HoloViz Projects serve different purposes in the ecosystem. Some are more foundational and have been in place for a long time, for instance, Colorcet or Param. Given their position, these Projects should be treated with extra care when it comes to backwards compatibility. For instance, maintainers of these Projects should favor making breaking changes in major releases and adopting longer deprecation periods. On the other hand, some Projects are newer and have an API that is still being gradually refined (e.g. Lumen). These Projects are not expected to be as stable, they change more quickly. 

Overall, the HoloViz Projects are known to be stable and their users have built this expectation. The functionalities they provide are generally not moved or removed lightly. Maintainers should aim to keep the Projects stable; moving or removing a feature from a code base **must** be motivated, in particular when it is done outside of a major release.

### Deprecation policy

#### Deprecation cycle guidelines

The following guidelines are meant to be consumed by maintainers of the Projects, who can use them as templates in PRs or while preparing a release. Note that while the goal of the HEP is to enforce a set of rules to ensure a more consistent deprecation cycle across the Projects, there will always be exceptions to the rules that this HEP does not prevent.

1. Before implementing a deprecation, maintainers:

  - [ ] **Must** motivate the best they can why the feature is deprecated (e.g. old and unused API) in an issue or in the *Pull Request* (PR) deprecating the feature.
  - [ ] **Must** reach a consensus among the maintainers of the Project on the deprecation.

2. Maintainers have to make sure that their users are well informed of the deprecation. They **must** implement the deprecation in the following way:

- [ ] Implement a programmatic warning, if not applicable the PR deprecating the feature **must** clearly explain why.

  - The warning **must** be emitted using one of these two utilities:
    - The `warn` function from the `warnings` module:

    ```python
    from warnings import warn

    def foo():
      warn(
        "Function foo is deprecated since version 1.1.1 and will be removed in a future release, use bar instead.",
        category=FutureWarning, stacklevel=2,
      )
      ...
    ```

    - The `deprecated` decorator added in Python 3.13 ([PEP 702](https://peps.python.org/pep-0702/)) to the `warnings` module, backported to previous Python versions via the [typing_extensions](https://github.com/python/typing_extensions).

    ```python
    from typing_extensions import deprecated

    @deprecated(
      "Function foo is deprecated since version 1.1.1 and will be removed in a future release, use bar instead.",
      category=FutureWarning,
    )
    def foo():
      ...
    ```

    The `deprecated` decorator not only emits a run-time warning, it also enables static type checkers to warn when they encounter usage of an object decorated with `deprecated`. This comes with various benefits, for example, VSCode users will see the deprecated objects crossed out in their code. Therefore, when possible, `deprecated` should be preferred over `warn`.

  - The warning message:

    - **Must** indicate that the feature is deprecated and is going to be removed in a future version.
    - **Must** suggest replacement APIs, if applicable.
    - Can indicate in which version the feature was deprecated.
    - Can indicate before which version the feature is going to be remove, however, maintainers should ensure that the deprecation period (see below) is not going to be too to short, and that no obsolete warning will be released (e.g. feature announced to be removed in version 1.1 but is still present in 1.1).

  - The warning type:
  
    - **Must** be a subclass of `DeprecationWarning`, `FutureWarning`, or `PendingDeprecationWarning`.
    - **Must** be defined based on this approach (see the Appendix for more details):

      1. Start by emitting a `DeprecationWarning`, to inform Library Developers, and some Data Analysts.
      2. After 12 months, upgrade to a `FutureWarning`, to inform all users.

      Exceptions are allowed but should in practice be very rare:

      - Start by emitting a `PendingDeprecationWarning` for deprecations that might be reverted or are expected to be extremely noisy.
      - Don't upgrade to a `FutureWarning` when the feature removed is meant for Library Developers only.
      - Emit directly a `FutureWarning` when the feature removed is meant for Data Analysts only.

  - `stacklevel` **must** be set so the warning appears in the correct place. Projects can implement a utiliy like the private Pandas' function [`find_stack_level`](https://github.com/pandas-dev/pandas/blob/b8a4691647a8850d681409c5dd35a12726cd94a1/pandas/util/_exceptions.py#L34) to automatically infer the right `stacklevel` number.

- [ ] Documentation: all usage of the deprecated feature **must** be removed from the documentation, except from the section that serves as the reference API. Special cases (e.g. major API change) will need extra documentation. When the deprecation involves the user having to change their code in a significant way (typically in a major release), maintainers should consider writing a migration guide.

3. When the deprecation is fully implemented, maintainers:

- [ ] **Must** make sure that the PR deprecating the feature is approved by at least another maintainer, who should check that the approach above has been followed.
- [ ] **Must** close all the open issues an PRs associated with the deprecated feature.

4. When releasing the deprecation, maintainers:

- [ ] **Must** include it in a major of minor release, not in a patch release.
- [ ] **Must** list the deprecated feature in the release notes.
- [ ] Are encouraged to list the Project's active deprecations (e.g. on the [website](https://github.com/holoviz/param/pull/922, in an *Issue*)) with enough information to infer when these deprecated features can be removed from the code base, and check regularly this listing not to miss the opportunity to remove a deprecated feature.

5. When removing the deprecated feature, maintainers:

  - [ ] **Must** ensure the removal isn't made *too soon* to let the maximum number of users find out about the deprecation. The recommendation is to observe a **minimum period of 6 months** between the release of the deprecation (a minimum period has been chosen in favor of a number of releases as no Project has adopted a regular release cadence).
  - [ ] **Must** include the change in a major or minor release, not in a patch release.
  - [ ] **Must** remove it from the code base and documentation.
  - [ ] **Must** mention the removal in the release notes.
  - [ ] **Must** close all open related issues and PRs.

#### Test suite guidelines

The Projects **must** be set up so that their test suite fails when they trigger deprecation warnings emitted by other HoloViz projects.

## Appendix: Detour on Python warnings applied to HoloViz

### Warning types

Python defines the following [warning types](https://docs.python.org/3/library/warnings.html#warning-categories):

| Class                     | Description                                                                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DeprecationWarning`        | Base category for warnings about deprecated features when those warnings are intended for other Python developers (ignored by default, unless triggered by code in `__main__`). |
| `FutureWarning`             | Base category for warnings about deprecated features when those warnings are intended for end users of applications that are written in Python.                               |
| `PendingDeprecationWarning` | Base category for warnings about features that will be deprecated in the future (ignored by default).                                                                         |

The warnings defined to be used when deprecating a feature are `DeprecationWarning`, `FutureWarning`, and `PendingDeprecationWarning`.

### Warnings filters and `stacklevel`

Python provides the `warnings` module whose `warn` function is usually called by developers to issue warnings. These warnings can be filtered by users when running some code. The default warning filter has the following entries (in order of precedence):

```
default::DeprecationWarning:__main__
ignore::DeprecationWarning
ignore::PendingDeprecationWarning
ignore::ImportWarning
ignore::ResourceWarning
```

Note that the default filters can be overriden by setting the `-W` flag when calling the `python` executable or via the `PYTHONWARNINGS` environment variable.

The default filters imply that in a regular context `PendingDeprecationWarning` will not be seen by the user while `FutureWarning` will always be seen. `DeprecationWarning` is treated specially, warnings of these types are only seen when they are triggered by and points to code in `__main__`, the latter depending on the value of `stacklevel`.

The `stacklevel` parameter of `warnings.warn` specifies how many levels of the call stack to skip when displaying the warning message, helping to identify the actual source of the warning in the code. Its default value is `1`, meaning that no level is skipped. Let's see how it works with a few examples:

```python
# mod1.py
import warnings

def foo():
    warnings.warn('The function foo is deprecated.')

foo()
```

Executing this script displays:

```
❯ python3 foo.py
/private/tmp/mod1.py:4: UserWarning: The function foo is deprecated.
  warnings.warn('The function foo is deprecated.')
```

While this doesn't look too bad, this is in fact far from being ideal as the user doesn't know from where `foo` was called from (it's trivial in this example, far less in large code bases!). The correct value for `stacklevel` in this case would be `2`:

```python
# mod1.py
import warnings

def foo():
    warnings.warn('The function foo is deprecated.', stacklevel=2)

foo()
```

Which displays the line where `foo` is called, making it a lot easier for the user to update their code:

```
/private/tmp/mod1.py:6: UserWarning: The function foo is deprecated.
  foo()
```

Let's now look at an example that will help us better understand when `DeprecationWarning`s are displayed or not:

```python
# mod1.py
from mod2 import bottom, top

print('Call top:')
top()

print('\nCall bottom:')
bottom()
```

```python
# mod2.py
import warnings

def top():
    return bottom()

def bottom():
    warnings.warn('bottom is deprecated', DeprecationWarning, stacklevel=2)
```

We run this code with `python mod1.py` which displays:

```
Call top:

Call bottom:
/private/tmp/mod1.py:8: DeprecationWarning: bottom is deprecated
  bottom()
```

Before diving into what happens line by line, note that `stacklevel` is set to `2` in the `bottom` function. This means that the warning will be associated to the line that called `bottom()`.

We first call `top()`, that calls `bottom()`, that emits a warning. This warning is associated with the line `return bottom()` in `mod2.py`. There, the module namespace is `mod2` and not `__main__`, so the `DeprecationWarning` **is not displayed**.

We then call `bottom()` which emits a warning associated with the line `bottom()` in `mod1.py`. Given how we ran this code with `python mod1.py`, the module namespace is `__main__` in `mod1.py`, so the `DeprecationWarning` **is displayed**. 

`stacklevel` affects greatly how `DeprecationWarning`s end up being displayed. Running the same code above with `stacklevel=1` (remember, that's its default value) leads to no warning being displayed, since they will all be associated to a code line in `mod2.py`. Setting `stacklevel=3` will display a warning when executing `top()` but not when executing `bottom()`. Since it is obviously easy to get this wrong, libraries like Pandas have developed their own [utility function](https://github.com/pandas-dev/pandas/blob/9008ee5810c09bc907b5fdc36fc3c1dff4a50c55/pandas/util/_exceptions.py#L34) to automatically infer the right value.


### `DeprecationWarning` and HoloViz users

As we saw above, `DeprecationWarning` is filtered in a special way, let's see what this means for HoloViz users.

#### Notebooks/scripts and utility modules/packages

The namespace value is `__main__` when users execute Python code in the REPL and in an IPython shell, which means that this also applies to code being run in Jupyter Notebooks, so this is identical to running a script with `python script.py`.

Take this simple example, where the user is working on a script or in a Notebook but is importing code from some utility module or a package they have implemented. The `my_panel_thing()` function is using a deprecated Panel pane that emits a `DeprecationWarning` when instantiated. The deprecation warning is going to be emitted in the scope of `util.py` where the module namespace is `util` and not `__main__`, therefore, it won't be displayed when they run the script or the notebook.

```python
# Untitled1039.ipynb
from util import my_panel_thing

my_panel_thing()
```

```python
# util.py
import panel as pn

def my_panel_thing():
  return pn.DeprecatedPane("YOLO")
```

#### Panel apps

Another important use case in the HoloViz ecosystem is deploying a Panel application. When an application is deployed with the `<panel serve ...` command, the module namespace of the served files is not `__main__` but is set internally to something like `bokeh_app_<uuid>`. The namespace of *setup* files (`--setup mysetup.py`) processed by Panel is also renamed internally. Therefore, Panel users serving their app with `panel serve` will not be able to see any warnings of type `DeprecationWarning`.

This can be easily verified serving this little app with `panel serve app.py`, the warning doesn't get displayed. Note it is possible to display it by serving the app with `python -Wdefault -m panel serve app.py`.

```python
# app.py
import warnings
import panel as pn

warnings.warn('Not displayed :(', DeprecationWarning)
pn.panel('Hello world!').servable()
```

#### Pytest

Pytest automatically catches all warnings during test execution and displays them at the end of the session. The issues listed above with `DeprecationWarning`s displayed only in a certain scope don't apply in this case, these warnings are always displayed by Pytest.


#### Two types of HoloViz users

We can define two types of HoloViz users:

- Library Developers: depend on HoloViz projects to develop their own library (this includes HoloViz projects themselves as they depend on each other, like Panel with Param)
- Data Analysts: use HoloViz projects to perform some sort of data analysis, often by writing code in a Notebook or in scripts they run directly or by building and serving a Panel app.

When a HoloViz project deprecates a feature and starts emitting a warning, it is possible it will impact both types of users, however they different wishes when it comes to deprecation warnings:

- Library Developers don't wish the warnings to be propagated to their own users, or at the very least not immediately. Instead, they will usually catch the warnings when running their test suite. They want to be given sufficient time to update and release their code, before the feature is removed or before the warning starts to be displayed to their own users.
- Data Analysts should be warned when a feature is deprecated but also should be given an easy way to hide these warnings.

`DeprecationWarning` is the warning type intended for other Python developers, it's certainly the warning type used the most in the Python ecosystem. However, as we've just seen, Data Analysts won't always be set up to see this warning.

#### Consequences

HoloViz users who:

- don't test their code with Pytest (quite likely for Data Analysts)
- and, don't override the default Python warning filters (even more likely)

won't be notified of `DeprecationWarning`s even if their code directly uses a feature emitting this warning when:

- they serve a Panel app with `panel serve`
- or, run a script/Notebook that imports a utility module/package that calls a deprecated feature emitting `DeprecationWarning`

### Outcome

Based on the fact that a non-negligeable fraction of HoloViz users may entirely miss `DeprecationWarning`s, we suggest adopting a tiered approach:

1. Start by emitting a `DeprecationWarning`, to inform Library Developers, and some Data Analysts.
2. After 12 months, upgrade to a `FutureWarning`, to inform all users.

Exceptions are allowed but should in practice be very rare:

- Start by emitting a `PendingDeprecationWarning` for deprecations that might be reverted or are expected to be extremely noisy.
- Don't upgrade to a `FutureWarning` when the feature removed is meant for Library Developers only.
- Emit directly a `FutureWarning` when the feature removed is meant for Data Analysts only.


## Copyright

This document is placed in the public domain or under the CC0-1.0-Universal license, whichever is more permissive.
