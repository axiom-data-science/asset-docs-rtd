import sys
import os
import sphinx_rtd_theme

sys.path.append(os.path.abspath('./_ext'))


project = 'Asset Docs RTD'
copyright = '2026, Axiom Data Science, LLC'
author = 'Dev'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    #'sphinxcontrib.bibtex',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinxcontrib.httpdomain',
    'gitlab_card',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'monokai'

todo_include_todos = True
todo_emit_warnings = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes"]
html_static_path = ['_static']

html_css_files = [
    'css/gitlab_card.css',
]
