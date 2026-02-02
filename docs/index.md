# Reproducible Research: Walking the Walk

A hands-on tutorial on reproducible research practices, originally presented
at [SciPy 2014](https://conference.scipy.org/scipy2014/) and updated for
modern tools and workflows.

## Description

This *hands-on* tutorial trains **reproducible research practitioners** on the
*practices and tools that make experimental verification possible with an
end-to-end data analysis workflow*. The tutorial covers open science methods
during data gathering, storage, analysis, and publication into a reproducible
article.

Attendees are expected to have basic familiarity with
[scientific Python](https://scipy.org) and [Git](https://git-scm.com).

## Quick Start

This project uses [uv](https://docs.astral.sh/uv/) for Python project
management.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and set up the project
git clone https://github.com/reproducible-research/scipy-tutorial-2014.git
cd scipy-tutorial-2014
uv sync

# Run the environment check
uv run python environment/check_env.py

# Launch JupyterLab to work through the notebooks
uv run jupyter lab

# Run the tests
uv run pytest
```

## Original Speakers

* Aashish Chaudhary
* Ana Nelson
* Jean-Christophe Fillion-Robin
* Luis Ibanez
* Matt McCormick
* Steve Smith

## Duration

The tutorial covers four hours, but *preparation is required*.

* [Required preparation](Preparation.md)
* [Agenda](agenda.md)
