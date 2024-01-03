# -*- coding: utf-8 -*-
import subprocess

from nbsite.shared_conf import *

project = "HoloViz"
authors = 'HoloViz authors'
copyright_years['start_year'] = '2017'
copyright = copyright_fmt.format(**copyright_years)
description = 'High-level tools to simplify visualization in Python.'

ret = subprocess.run([
    'git', 'describe', '--long', '--match', "v[0-9]*.[0-9]*.[0-9]*", '--dirty'
], text=True, capture_output=True, check=True)
version = release  = base_version(ret.stdout.strip()[1:])

exclude_patterns = ['governance/project-docs/*.md']

html_static_path += ['_static']

html_theme = "pydata_sphinx_theme"
html_logo = '_static/holoviz-logo-unstacked.svg'
html_favicon = "_static/favicon.ico"

html_theme_options.update({
    "github_url": "https://github.com/holoviz/holoviz",
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/HoloViz_Org",
            "icon": "fab fa-twitter-square",
        },
        {
            "name": "Discourse",
            "url": "https://discourse.holoviz.org/",
            "icon": "fab fa-discourse",
        },
    ],
    "header_links_before_dropdown": 6,
    "secondary_sidebar_items": [
        "github-stars-button",
        "page-toc",
    ],
})

html_context.update({
    # Used to add binder links to the latest released tag.
    'last_release': f'v{release}',
    'github_user': 'holoviz',
    'github_repo': 'holoviz',
})
