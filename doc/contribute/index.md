# General Contributing Guidelines

This guide includes general guidelines on how to contribute to HoloViz. Read the [Operating Guide](#operating-guide) if you are interested in learning how an Open-Source project like HoloViz operates.

## Contributing? Yes! Wait, but why?

There are many reasons why you would want to contribute to the HoloViz project, including:

* You appreciate the HoloViz project, its mission and values, and would like to help
* You are a user of one of the HoloViz packages and need a bug to be fixed or a new feature to be implemented, and you are willing to tackle that in some ways
* You are looking for some open-source experience
* You have been reading one of the HoloViz websites and found something to improve, even just a simple typo

These reasons, or whatever reason brought you here, are all valid in our eyes. We **welcome anyone** who wishes to contribute, and as you will see, there are **many** ways to contribute!

```{hint}
Contributing to the HoloViz project might even get you a job, which has been the case for a couple of HoloViz members.
```

## Using AI README

**Maintainers are humans and have finite time and energy to review contributions**. As such, they need to prioritize their work, and they may not have the time to review all contributions. We will be especially reluctant to take time to review submissions that seem to be of low effort on the part of the submitter. Conversely, we especially value contributions that arise from real user use cases, i.e. actually using HoloViz packages like Lumen, Panel, HoloViews, hvPlot, Datashader, and others to build something you care about, but encounter a bug or missing feature.

If you are a new contributor and are contributing a PR though, you can use AI tools, **but you must follow these rules in the PR description**:

- Follow the repos' PR template
- Explain what motivated the PR (were you trying to achieve something, but encountered ...?)
- Do NOT list out what changed, unless you want to bring attention to specific changes
- Include reproduction steps, ideally a Minimal Reproducible Verifiable Example
- Screenshots or screen recordings (before changes and after changes) must be included
- Cite sources and docs you referenced with working links
- Do NOT copy full output of AI summary and instead curate a description yourself

Please limit to 2 open PRs at a time across our repos; if you have more than 2 open PRs, they may be closed, especially if it is your first time contributing to HoloViz.

Separately, please refrain from tagging maintainers shortly after opening a PR/issue, as reviews will happen when time allows. Only bump a PR/issue that has been open for a longer period of time (weeks) without a response.

Maintainers reserve the right to close PRs they deem low-effort or AI-generated without review.

Remember, contributions don't just have to be Pull Request(s) (PR)s either! Filing bugs, helping others on Discord or Discourse, writing blog posts, or sharing things you built on social media all count! See below for more ideas!

As an example, Andrew saw a cool chart online and tried to reproduce it with HoloViews, but noticed that the labels' text color doesn't cycle through alongside the points' color. This motivated him to [create an issue to report it](https://github.com/holoviz/holoviews/issues/5887) and separately [create a PR to fix it](https://github.com/holoviz/holoviews/pull/5888).

Let's continue building a meaningful community!

## What and how to contribute?

If you end up on this page it is quite likely that you are interested in contributing code to HoloViz. However, as you will see, there are many other areas where you could contribute, and in some of these areas, the HoloViz project would really appreciate some help!

### Documentation

Each core HoloViz package has its own website. Maintaining the content of these websites is a lot of work, and you can easily help by:

* Submitting a Pull Request (PR) to fix a typo
* Submitting a PR to clarify a section
* Submitting a PR to document an undocumented feature
* Submitting a PR to update a section that should have been updated

How the websites look and feel can also be improved. If you happen to have some front-end development expertise, your help would be greatly appreciated.

Finally, the documentation also lies within the code, and in Python, it is found in the so-called *docstrings* that accompany modules, classes, methods and functions. You can easily improve the docstrings by:

* Submitting a PR to fix a typo
* Submitting a PR to clarify a definition
* Submitting a PR to fix or document the default value of a parameter

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
The HoloViz projects usually provide specific instructions on how to set up your environment to be ready to contribute documentation or code to the project. The instructions provided hereafter are meant to be general enough to apply to each project. Refer to the documentation of the project you are working on for more details.
```

Before making anything beyond a minimal contribution (e.g., fixing a typo), the first step is usually to open a [GitHub Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) that documents what you are trying to fix/improve. Writing a good issue is important and will affect how it is going to be perceived by the project maintainers, contributors and watchers. Read for instance this [blog post](https://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports) that describes what a good issue should look like.  Once an issue is opened, a discussion can take place with the maintainers to see if what is suggested is relevant, which can guide the next steps.

#### Getting Started

The first step to working on any source code is to install Git as the source codes are stored in [Git](https://git-scm.com) source control repositories. To install Git on any platform, refer to the [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) section of the [Pro Git Book](https://git-scm.com/book/en/v2).

As an external contributor, you do not have permission to submit code directly to any of the repositories. Github offers you the ability to fork the repository, which will create a copy of the repository, on which you will have the right to work freely. Follow [these instructions](https://docs.github.com/en/get-started/quickstart/fork-a-repo) to find out how to fork and clone a repository.

#### Environment Setup

The HoloViz developers rely on [Pixi](https://pixi.sh/latest), a developer tool that facilitates maintaining all of the HoloViz projects. See [Pixi](#pixi-guide) for more details.

#### Contributing Changes

After you have cloned the repo and set up Pixi, the next step is to create a branch and start making changes. Before committing these changes, make sure the tests still pass by running `pixi run test-unit` and that the code meets style guidelines by running `pixi run lint`. Once you are done with your changes, you can commit them. It is good practice to break down big changes into smaller chunks, and each chunk has its own commit with a message that summarizes it.

#### Submitting Your Contribution

Now you can push the branch to your clone and create a *pull request* from your clone to the original repository. This [Github Gist](https://gist.github.com/Chaser324/ce0505fbed06b947d962) describes these GitHub steps in more detail.

The *pull request* you make should reference the *issue* you are attempting to close (i.e. `Fixes #issuenumber`) and include a description of the changes you made.
See [linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) for more detailed instructions on how to do that. Changes affecting the visual properties should include screenshots or GIFs.

Your *pull request* should now be reviewed by one of the project's maintainers. This may take a while given how busy the maintainers are, so try to be patient :). Your pull request will be evaluated to ensure that it is within the scope of the project (again, it's a good idea to create an issue first to outline your intent and give the maintainers an opportunity to weigh in before you spend the effort creating a pull request). If it's decided to proceed, the review will be conducted, and once the review is done you may be required to make some changes. You may also be asked to *resolve conflicts* if the changes you made appear to conflict with changes made to the source code after you submitted the *pull request*.

When your PR is merged, enjoy, and repeat!

```{toctree}
:maxdepth: 2
:hidden:
:titlesonly:

General Contributing Guidelines <self>
Operating guide for maintainers <operating_guide>
```
