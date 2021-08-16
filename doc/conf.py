# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = u"HoloViz"
authors = u'HoloViz authors'
copyright = u'\u00a9 2017-2019, ' + authors
description = 'High-level tools to simplify visualization in Python.'

import holoviz
version = release = holoviz.__version__

html_static_path += ['_static']

html_css_files = [
    'nbsite.css',
    'css/custom.css'
]

html_theme = "pydata_sphinx_theme"
html_logo = '_static/holoviz-logo.svg'
html_favicon = "_static/favicon.ico"

html_theme_options = {
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
}

templates_path = ['_templates']

html_context.update({
    "github_user": "holoviz",
    "github_repo": "holoviz",
})
