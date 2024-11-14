# -*- coding: utf-8 -*-
import subprocess

from nbsite.shared_conf import *

from bs4 import BeautifulSoup
from sphinx import addnodes

# def html_page_context(app, pagename, templatename, context, doctree):
#     """Event handler for the html-page-context signal."""
#     # Only generate TOC for the 'index' page
#     if pagename == "index":
#         rendered_toc = build_and_render_full_toc(app.builder)
#         # Add structured TOC to the template context
#         context['custom_toc'] = parse_toc_html(rendered_toc)

import pprint

def html_page_context(app, pagename, templatename, context, doctree):
    # Only generate TOC for the 'index' page
    if pagename == "index":
        rendered_toc = build_and_render_full_toc(app.builder)
        parsed_toc = parse_toc_html(rendered_toc)
        
        # Print the structure to verify it's correct
        print("Custom TOC Structure:")
        pprint.pprint(parsed_toc)
        
        # Add structured TOC to the template context
        context['custom_toc'] = parsed_toc


def build_and_render_full_toc(builder):
    """Build and render the full TOC HTML from the master document."""
    env = builder.env
    master_doc = env.config.master_doc
    doctree = env.get_doctree(master_doc)
    toctrees = []

    # Traverse the master document for all toctree nodes and resolve them
    for toctreenode in doctree.traverse(addnodes.toctree):
        resolved_toctree = env.resolve_toctree(master_doc, builder, toctreenode, collapse=False, includehidden=True)
        if resolved_toctree:
            toctrees.append(resolved_toctree)

    # Combine all toctree nodes into a single document
    if not toctrees:
        return ''
    combined_toc = toctrees[0]
    for toctree in toctrees[1:]:
        combined_toc.extend(toctree.children)
    
    # Render the combined TOC as HTML
    return builder.render_partial(combined_toc)['fragment']

def parse_toc_html(toc_html):
    """Parse the TOC HTML with BeautifulSoup and convert it to a structured list."""
    def ul_to_list(node):
        """Recursively convert a TOC <ul> element to a list of dictionaries."""
        out = []
        for child in node.find_all("li", recursive=False):
            formatted = {}
            link = child.find("a", recursive=False)
            if link:
                formatted["title"] = link.text.strip()
                formatted["href"] = link.get("href", "#")
            else:
                formatted["title"] = "Untitled"
                formatted["href"] = "#"
            
            # If there is a nested <ul>, process it recursively as children
            sublist = child.find("ul", recursive=False)
            if sublist:
                formatted["children"] = ul_to_list(sublist)
            else:
                formatted["children"] = []
            
            out.append(formatted)
        return out

    try:
        soup = BeautifulSoup(toc_html, "html.parser")
        ul = soup.find("ul")
        if ul:
            return ul_to_list(ul)
        return []
    except Exception as exc:
        print(f"Failed to parse TOC: {exc}")
        return []

def setup(app):
    app.connect('html-page-context', html_page_context)


project = "HoloViz"
authors = 'HoloViz authors'
copyright_years['start_year'] = '2017'
copyright = copyright_fmt.format(**copyright_years)
description = 'High-level tools to simplify visualization in Python.'

ret = subprocess.run([
    'git', 'describe', '--long', '--match', "v[0-9]*.[0-9]*.[0-9]*", '--dirty'
], text=True, capture_output=True, check=True)
version = release  = base_version(ret.stdout.strip()[1:])

extensions += [
    'nbsite.analytics',
]

html_static_path += ['_static']
templates_path += ['_templates']

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
    # custom navbar template
    "navbar_center": ["navbar.html"],
    "show_nav_level": 1,
})

html_context.update({
    # Used to add binder links to the latest released tag.
    'last_release': f'v{release}',
    'github_user': 'holoviz',
    'github_repo': 'holoviz',
})

# Uncomment to turn off notebook execution.
nb_execution_mode = "off"

nbsite_analytics = {
    'goatcounter_holoviz': True,
}
