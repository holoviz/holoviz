# HEP 2: Release and deprecation policies

This HEP describes the release and deprecation policies adopted by the HoloViz Projects. The overall goal of this HEP is to ensure that these policies are consistently applied across the Projects, which will help provide a consistent user experience and help contributors and maintainers make decisions (in particular when dealing with a project they are not very familiar with). The HEP formalizes as a set of practices adopted over time and also introduces a few more rules (e.g. minimum deprecation period).

## Versioning

The Projects deliver final releases with a version number of the form `<major>.<minor>.<patch>` (e.g. `1.2.3`):

- `patch` releases (e.g. 0.1.**0** -> 0.1.**1**) should never intentionally and rarely, if ever, unintentionally break API. Should be safe to upgrade to the latest patch release if you encounter any problems.
- `minor` releases (e.g. 0.**1**.1 -> `0.**2**.0) should not have API changes that affect most users. API changes in minor releases should be rare, but are not unheard of, particularly for recently added functionality whose API is still being refined, or for bugs found in older code that can't be fixed without changing API at least slightly.
- `major` releases (e.g. **0**.2.0 -> **1**.0.0)  will typically break APIs, but should normally include significant new functionality to motivate users to update their code. Major breaking API changes should be postponed to a major release and paired with significant user-visible advantages.

While this versioning scheme is inspired by [Semantic Versioning](https://semver.org/) (*SemVer*), like many other Python projects, **the HoloViz Projects do not strictly follow it** as incompatible (aka breaking) API changes are not limited to `major` releases.

The Projects can deliver three types of pre-releases / development versions:

- `alpha` (e.g. `1.2.3a1`): Projects can deliver alpha releases for users to benefit from and/or test bug fixes and new features, early in the development phase of a new version. alpha releases are common across the Projects.
- `beta` (e.g. `1.2.3b1`): Projects can deliver beta releases for the same reasons, except they indicate the project is in a more advanced development phase of a new version. beta releases are not common across the Projects, they're more likely to be useful when a major release is in development, to progressively deliver large new features and API breaking changes.
- `release candidate` (e.g. `1.2.3rc1`): Projects must deliver a release candidate version before the final release.

## Supported versions

Exception in certain exceptional cases, the Projects do not backport changes to previous major or minor releases.

## Release process

Releasing a new version consists of packaging the software and distributing it. The Projects are set up to automatically perform this process on a Continuous Integration (CI) system (e.g. Github Actions). The process is triggered automatically when a new tag (of the form `v1.2.3`) is pushed to the Git repository. The tag message should be of the form `Version x.x.x` for final releases and `Version x.x.x. alpha1/beta1/RC1` for pre-releases.

## Distribution

HoloViz maintainers are responsible for distributing the Projects on these platforms:

- Pre-releases are distributed on [PyPI](https://pypi.org) and on the *pyviz/label/dev* channel of [Anaconda.org](https://anaconda.org).
- Final versions are distributed on [PyPI](https://pypi.org), and on the  *conda-forge* and *defaults* channels of [Anaconda.org](https://anaconda.org).

## Release cadence

The Projects have not adopted a regular release cadence, a new release happens whenever maintainers find it is appropriate. A Project is free to adopt a regular release cadence.

Major regressions in a release should be fixed and released in a new patch version as soon as possible.

## Deprecation and removal policy

The Projects can deprecate a feature in any type of final release (patch, minor, or major). Maintainers have to make sure that their users are well informed of the deprecation. They **must** mention the deprecation in the following ways:

- Programmatic warning: The `warnings` module from the standard library must be used to emit a deprecation warning (`import warnings; warnings.warn(...)`). The warning message must indicate that the feature is deprecated (it can indicate which version deprecated it) and that it is going to be removed in a future version, without indicating in which version exactly (see why below). The warning type must be a subclass of `DeprecationWarning`, `PendingDeprecationWarning`, or `FutureWarning`. `stacklevel` must be set so the warning appears in the correct place. For example:  `warnings.warn('Function foo is deprecated since Panel 1.2.3 and will be removed in a future release, use bar instead.', DeprecationWarning, stacklevel=3)`. When a programmatic warning cannot be implemented, the *Pull Request* deprecating the feature must clearly explain why.
- Docstring (if applicable): the docstring of the deprecated feature must be updated to mention the deprecation, when possible the [`deprecated`](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-deprecated) Sphinx directive should be used.
- Documentation: all usage of the deprecated feature must be removed from the documentation, except from the section that serves as the reference API. Special cases (e.g. major API change) will need extra documentation.
- Release notes: the release notes must list the deprecated feature.

When a feature has been deprecated, its warning and documentation must stay in place for some time long enough to let most users find out about it. For example, Panel users who lock the dependencies of their application should be given sufficient time between the deprecation of a feature and its removal so as not to miss the deprecation warnings and be left with broken code, once they attempt to upgrade their version of Panel to the latest. A deprecated feature **can only be removed 18 months after users have been informed of its deprecation**. This period, introduced by this HEP, factors in the facts that:

- Users cannot build expectations about when in time a feature is going to be removed if the deprecation indicates a version number (e.g. `'This feature will be removed in version 1.2.3'`) as the Projects don't release new versions based on a regular cadence.
- Many HoloViz users are not professional software developers/engineers, they use Python to help them accomplish their work and as such touch code less frequently.

Maintainers are encouraged to create a table of deprecated features (e.g. in an *Issue*) that includes the dates after which these features can be removed, and check regularly this table not to miss the opportunity to remove a deprecated feature.

## Backwards compatibility

The HoloViz Projects serve different purposes in the ecosystem. Some are more foundational and have been in place for a long time, this includes for instance Colorcet or Param. Given their position, these Projects should be treated with extra care when it comes to backwards compatibility. For instance, maintainers of these Projects should favor making breaking changes in major releases and adopting longer deprecation periods. On the other hand, some Projects are newer and have an API that is still being gradually refined (e.g. hvPlot). These Projects are not expected to be as stable, they change more quickly. 

Overall, the HoloViz Projects are known to be stable and their users have built this expectation. The functionalities they provide are generally not moved or removed lightly. Maintainers should aim to keep the Projects stable, moving or removing a feature from a code base must be motivated by a significant maintenance cost, in particular when it is done outside of a major release.
