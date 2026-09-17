Asset Docs RTD
==============


A Read-the-Docs (RTD) repository housing information specific to building and
operating the suite of Asset Docs components.

Copyright 2026, Axiom Data Science, LLC

See LICENSE for details.


Building the Documentation
--------------------------

To set up a local environment with `uv`_, create a virtual environment and
install the documentation dependencies::

    uv venv
    uv pip install -r requirements.txt
    source .venv/bin/activate

There is a `Makefile` available which can be used to compile the source documents into the HTML product viewable by web browsers::

    make html

The command produces a compiled product under the `build` directory.

.. _uv: https://docs.astral.sh/uv/
