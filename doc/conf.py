# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = "HoloViz"
authors = 'HoloViz authors'
copyright_years['start_year'] = '2017'
copyright = copyright_fmt.format(**copyright_years)
description = 'High-level tools to simplify visualization in Python.'

import holoviz
version = release  = base_version(holoviz.__version__)

html_static_path += ['_static']

html_css_files = [
    'nbsite.css',
    'css/custom.css'
]

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
    ]
})

templates_path += ['_templates']

html_context.update({
    # Used to add binder links to the latest released tag.
    'last_release': f'v{release}',
    'github_user': 'holoviz',
    'github_repo': 'holoviz',
})
