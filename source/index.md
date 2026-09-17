# Asset Docs Technical Documentation

Asset Docs is a general and extensible stack of software for creating
validatable structured documents (JSON documents, validated by a JSON Schema)
that can be used to facilitate metadata collection for scientific datasets.

This project is maintained by [Axiom Data Science (AXDS)][axds] (a
[Tetratech][tetratech] company).

## Welcome!

This is the Asset Docs technical docuemntation. The purpose of
this document collection is to help you with the following:

*   To understand the broad purpose of the Asset Docs stack.

*   To provide guidance for building and setting up your own Asset Docs
    instance.

*   To answer questions that may come up when operating an Asset Docs instance.

## Getting Started

To get started, please see the following:

*   [INSTALL](doc/INSTALL)


## Reference Repositories

These repositories are those that are required for setting up an instance of
Asset Docs.

*   [asset-docs-postgres-db][adpdb], repo for the backend/database for Asset
    Docs powered by [PostgREST](https://docs.postgrest.org/).

*   [asset-manager][am], a frontend for Asset Docs allowing for the rapid
    development of forms and schemas.


## Table of Contents

```{toctree}
---
maxdepth: 3
---
doc/INSTALL
doc/CONFIG
doc/ARCHITECTURE
```

[axds]: https://www.axiomdatascience.com/
[tetratech]: https://www.tetratech.com/

[adpdb]: https://github.com/axiom-data-science/asset-docs-postgres-db
[am]: https://github.com/axiom-data-science/asset-manager
