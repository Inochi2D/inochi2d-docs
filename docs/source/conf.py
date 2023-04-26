# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from gettext import gettext
import os
import sphinx_rtd_theme


project = 'Inochi2D'
copyright = '2022, Luna the Foxgirl'
author = 'Luna the Foxgirl'
release = '0.7'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx_tabs.tabs",
    "sphinxext.opengraph",
]

templates_path = ['_templates']
exclude_patterns = []

# Translation
gettext_uuid = True
gettext_compact = False



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_css_files = [
    "css/style.css",
]

html_js_files = [
    "js/instant.js",
]

html_static_path = ["_static"]
html_logo = "_static/inochi2d.png"
html_favicon = "_static/favicon.ico"


# Theme options
html_theme_options = {

    # if we have a html_logo below, this shows /only/ the logo with no title text
    "logo_only": True,

    # Collapse navigation (False makes it tree-like)
    "collapse_navigation": False,
}

# Translation options
locale_dirs = ["locale/"]
gettext_compact = False