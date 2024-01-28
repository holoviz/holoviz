# HEP 2: Release and deprecation policies

This HEP describes the release and deprecation policies adopted by the HoloViz Projects. While two HEPs could have be written to describe these policies separately, it is deemed that they are enough intertwined to be addressed together (e.g. in which kind of final release can a feature be deprecated/removed?).

The overall goal of the HEP is to ensure that these policies are **consistently applied across the Projects**, which will help provide a **consistent user experience** and **help contributors and maintainers make decisions**.

The Projects already follow a pretty consistent procedure when it comes to releases, which this HEP formalizes. However, the Projects have applied various approaches for their deprecation cycle, the HEP introduces new and well defined guidelines. Making it easier for Projects to deprecate features is **key to their long-term maintenance**.

## Release policy

### Versioning

The Projects deliver final releases with a version number of the form `<major>.<minor>.<patch>` (e.g. `1.2.3`):

- `patch` releases (e.g. 0.1.**0** -> 0.1.**1**) should never intentionally and rarely, if ever, unintentionally break API. Should be safe to upgrade to the latest patch release if you encounter any problems.
- `minor` releases (e.g. 0.**1**.1 -> 0.**2**.0) should not have API changes that affect most users. API changes in minor releases should be rare, but are not unheard of, particularly for recently added functionality whose API is still being refined, or for bugs found in older code that can't be fixed without changing API at least slightly.
- `major` releases (e.g. **0**.2.0 -> **1**.0.0)  will typically break APIs, but should normally include significant new functionality to motivate users to update their code. Major breaking API changes should be postponed to a major release and paired with significant user-visible advantages.

While this versioning scheme is inspired by [Semantic Versioning](https://semver.org/) (*SemVer*), like many other Python projects, **the HoloViz Projects do not strictly follow it** as incompatible (aka breaking) API changes are not limited to `major` releases.

The Projects can deliver three types of pre-releases / development versions:

- `alpha` (e.g. `1.2.3a1`): Projects can deliver alpha releases for users to benefit from and/or test bug fixes and new features, early in the development phase of a new version. alpha releases are common across the Projects.
- `beta` (e.g. `1.2.3b1`): Projects can deliver beta releases for the same reasons, except they indicate the project is in a more advanced development phase of a new version. beta releases are not common across the Projects, they're more likely to be useful when a major release is in development, to progressively deliver large new features and API breaking changes.
- `release candidate` (e.g. `1.2.3rc1`): Projects must deliver at least one release candidate version before the final release and Projects should not add new features between release candidates. There is no expectation from Projects to announce their release candidates to a wide audience and wait some time before making a final release. However, Projects are encouraged to adopt that approach when they prepare an important release, typically a major or a significant minor release.

### Supported versions

Aside from certain exceptional cases, the Projects do not backport changes to previous major or minor releases.

### Distribution

HoloViz release managers are responsible for distributing the Projects on these platforms:

- Pre-releases are distributed on [PyPI](https://pypi.org) and on the *pyviz/label/dev* channel of [Anaconda.org](https://anaconda.org).
- Final versions are distributed on [PyPI](https://pypi.org), and on the  *conda-forge* and *defaults* channels of [Anaconda.org](https://anaconda.org).

### Release cadence

The Projects have not adopted a regular release cadence; a new release happens whenever maintainers find it is appropriate. A Project is free to adopt a regular release cadence.

Major regressions in a release should be fixed and released in a new patch version as soon as possible.

## Backwards compatibility

The HoloViz Projects serve different purposes in the ecosystem. Some are more foundational and have been in place for a long time, this includes for instance Colorcet or Param. Given their position, these Projects should be treated with extra care when it comes to backwards compatibility. For instance, maintainers of these Projects should favor making breaking changes in major releases and adopting longer deprecation periods. On the other hand, some Projects are newer and have an API that is still being gradually refined (e.g. hvPlot). These Projects are not expected to be as stable, they change more quickly. 

Overall, the HoloViz Projects are known to be stable and their users have built this expectation. The functionalities they provide are generally not moved or removed lightly. Maintainers should aim to keep the Projects stable; moving or removing a feature from a code base must be motivated by a significant maintenance cost, in particular when it is done outside of a major release.

## Deprecation policy

### Background

The goal of deprecating a feature is often to reduce the long-term maintenance burden of a Project. However, the act itself of deprecating a feature - the deprecation cycle - is a process that requires many actions be undertaken by the maintainers of a Project, starting from when they begin discussing the deprecation to when they remove the deprecated feature, which will potentially be done by other maintainers multiple years later. Given the complexity of the process and its somewhat remote benefits, without clear guidelines it's easy for maintainers to make mistakes, potentially affecting the user experience.

At the time of writing this HEP the Projects do not have a clear plan for their deprecation cycle. They also often adopt non-standard practices. For instance, many Projects display deprecation warnings using the logging API provided by Param (`param.main.param.warning(...)`), while in the Python ecosystem it is much more common to user the function `warnings.warn` from the standard library. With this function, users can easily control the behavior of these warnings (e.g. hide them, turn them into errors).

### Deprecation cycle guidelines

The Projects can deprecate a feature in any type of final release (patch, minor, or major). However, before implementing the deprecation, they **must**:

- Motivate the best they can why the feature is deprecated (e.g. old and unused API) in an issue or in the *Pull Request* (PR) deprecating the feature.
- Reach a consensus among the maintainers of the Project on the deprecation.
- Make sure that PR deprecating the feature is approved by at least another maintainer, who should check that the indications below have been followed.

 Maintainers have to make sure that their users are well informed of the deprecation. They **must** mention the deprecation in the following ways:

- Programmatic warning: The `warnings` module from the standard library must be used to emit a deprecation warning (`import warnings; warnings.warn(...)`). The warning message must indicate that the feature is deprecated (it can indicate which version deprecated it) and that it is going to be removed in a future version, without indicating in which version exactly (see why below). The warning type must be a subclass of `DeprecationWarning`, `PendingDeprecationWarning`, or `FutureWarning`. `stacklevel` must be set so the warning appears in the correct place. For example:  `warnings.warn('Function foo is deprecated since Panel 1.2.3 and will be removed in a future release, use bar instead.', DeprecationWarning, stacklevel=3)`. When a programmatic warning cannot be implemented, the PR deprecating the feature must clearly explain why.
- Docstring (if applicable): the docstring of the deprecated feature must be updated to mention the deprecation; when possible the [`deprecated`](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-deprecated) Sphinx directive should be used.
- Documentation: all usage of the deprecated feature must be removed from the documentation, except from the section that serves as the reference API. Special cases (e.g. major API change) will need extra documentation.
- Release notes: the release notes must list the deprecated feature.
- Repository: all the open issues an PRs associated with the deprecated feature must be closed.

When the deprecation involves the user having to change their code in a significant way (typically in a major release), maintainers should consider writing a migration guide.

When a feature has been deprecated, its warning and documentation must stay in place for some time long enough to let most users find out about it. For example, Panel users who lock the dependencies of their application should be given sufficient time between the deprecation of a feature and its removal so as not to miss the deprecation warnings and be left with broken code, once they attempt to upgrade their version of Panel to the latest. A deprecated feature **can only be removed 18 months after users have been informed of its deprecation**. This period, introduced by this HEP, factors in the facts that:

- Users cannot build expectations about when in time a feature is going to be removed if the deprecation indicates a version number (e.g. `'This feature will be removed in version 1.2.3'`) as the Projects don't release new versions based on a regular cadence.
- Many HoloViz users are not professional software developers/engineers; they use Python to help them accomplish their work and as such touch code less frequently.

Maintainers are encouraged to create a table of deprecated features (e.g. in an *Issue*) that includes the dates after which these features can be removed, and check regularly this table not to miss the opportunity to remove a deprecated feature.

When the time to remove the deprecated feature has come, maintainers **must**:

- Remove it from the code base and documentation.
- Mention the removal in the release notes.
- Include the change in a major or minor release.
- Close all open related issues and PRs.

### Detour on Python warnings

Python provides the `warnings` module whose `warn` function is usually called by developers to issue warnings. These warnings can be filtered by users running the code. The default warning filter has the following entries (in order of precedence):

```
default::DeprecationWarning:__main__
ignore::DeprecationWarning
ignore::PendingDeprecationWarning
ignore::ImportWarning
ignore::ResourceWarning
```

The default filters imply that in a regular context `PendingDeprecationWarning` will not be seen by the user while `FutureWarning` will always be seen. `DeprecationWarning` is treated specially, warnings of these types are only seen when they are triggered by and points to code in `__main__`, the latter depending on the value of `stacklevel`.

The `stacklevel` parameter of `warnings.warn` specifies how many levels of the call stack to skip when displaying the warning message, helping to identify the actual source of the warning in the code. Its default value is `1`, meaning that no level is skipped. Let's see how it works with a few examples:

```python
# mod1.py
import warnings

def foo():
    warnings.warn('The function foo is deprecated, use foo2().')

foo()
```

Executing this script displays:

```
❯ python3 foo.py
/private/tmp/mod1.py:4: UserWarning: The function foo is deprecated, use foo2().
  warnings.warn('The function foo is deprecated, use foo2().')
```

While this doesn't look too bad, this is in fact far from being ideal as the user doesn't know from where `foo` was called from (it's trivial in this example, far less in large code bases!). The correct value for `stacklevel` in this case would be `2`:

```python
# mod1.py
import warnings

def foo():
    warnings.warn('The function foo is deprecated, use foo2().', stacklevel=2)

foo()
```

Which displays the line where `foo` is called, making it a lot easier for the user to update their code:

```
/private/tmp/mod1.py:6: UserWarning: The function foo is deprecated, use foo2().
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

Given how we ran the code the namespace (`__name__`) of `mod1.py` is `__main__`, which is what allows `DeprecationWarning`s to be displayed. However, calling `top()` didn't display any `DeprecationWarning` as the warning is associated to a code line in `mod2.py` and not `mod1.py` (`__main__`). Calling `bottom()` did show the warning as its associated call line is in `__main__`.

`stacklevel` affects greatly how `DeprecationWarning`s end up being displayed. Running the same code above with `stacklevel=1` (remember, that's its default value) leads to no warning being displayed, since they will all be associated to a code line in `mod2.py`. Setting `stacklevel=3` will display a warning when executing `top()` but not when executing `bottom()`. Since it is obviously easy to get this wrong, libraries like Pandas have developed their own [utility function](https://github.com/pandas-dev/pandas/blob/9008ee5810c09bc907b5fdc36fc3c1dff4a50c55/pandas/util/_exceptions.py#L34) to automatically infer the right value.

The namespace is also `__main__` when users execute Python code in the REPL and in an IPython shell, which means that this also applies to code being run in Jupyter Notebooks. This is important to note as HoloViz users often run their code directly in a notebook.

The namespace **is not `__main__`** in files served by Panel/Bokeh as their namespace is set to `bokeh_app_<uuid>` internally. The namespace of *setup* files (`--setup mysetup.py`) processed by Panel is also renamed internally.

```python
# app.py
import warnings
import panel as pn

warnings.warn('Not displayed :(', DeprecationWarning)
pn.panel('Hello world!').servable()
```

Serving the app above with `panel serve app.py` will not show the warning. It is possible to display it by serving the app with `python -Wdefault -m panel serve app.py`.

...
