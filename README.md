# Asset Docs RTD


A Read-the-Docs (RTD) repository housing information specific to building and
operating the suite of Asset Docs components.

Copyright 2026, Axiom Data Science, LLC

See LICENSE for details.


## Building the Documentation

To set up a local environment with [uv][_uv], create a virtual environment and
install the documentation dependencies::

```shell
uv venv
uv pip install -r requirements.txt
source .venv/bin/activate
```

There is a `Makefile` available which can be used to compile the source documents into the HTML product viewable by web browsers::

```shell
make html
```

The command produces a compiled product under the `build` directory.

Live Preview (sphinx-autobuild)
-------------------------------

If you would like to develop locally, you can use the `sphinx-autobuild` utility
to automatically build, host, and refresh any connected web browser to view
new content.

```shell
mkdir -p ./build && sphinx-autobuild ./source/ ./build/
```

...then browse to:

<http://127.0.0.1:8000>

---

[_uv]: https://docs.astral.sh/uv/
