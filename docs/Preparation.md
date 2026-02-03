# Preparation

This document describes the steps required to prepare for this tutorial.

## Prerequisites

* Basic familiarity with Python and the scientific Python stack
* Basic familiarity with Git and the command line
* A GitHub account

## Install uv

[uv](https://docs.astral.sh/uv/) is the recommended Python package and project
manager. Install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Clone a Fork of the Tutorial Repository

[![GitHub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){ width="100" }](https://github.com)

1. [Sign up](https://github.com/join) for a free [GitHub](https://github.com) account.
2. [Create a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) of [the tutorial repository](https://github.com/reproducible-research/scipy-tutorial-2014).
3. Clone the fork locally:

```bash
git clone git@github.com:<your-username>/scipy-tutorial-2014.git
cd scipy-tutorial-2014
```

## Set Up the Environment

Install all dependencies with a single command:

```bash
uv sync
```

This will:

* Install Python 3.13 if needed (uv manages Python versions)
* Create a virtual environment
* Install all project dependencies (NumPy, SciPy, Matplotlib, SimpleITK, JupyterLab, pytest, etc.)

## Validate Your Environment

Run the environment check script:

```bash
uv run python environment/check_env.py
```

You should see `Success. All dependencies are available.`

## Sign Up for a Figshare Account

[![Figshare logo](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Figshare_logo.svg/200px-Figshare_logo.svg.png){ width="150" }](https://figshare.com)

[Sign up](https://figshare.com/account/register) for a free
[Figshare](https://figshare.com) account. We will use this to share and
download data during the tutorial.

## Work Through the First Notebook

Launch JupyterLab and work through the [01-SimpleITK-Filtering](https://nbviewer.org/github/reproducible-research/scipy-tutorial-2014/blob/master/notebooks/01-SimpleITK-Filtering.ipynb) notebook
to verify everything is working:

```bash
uv run jupyter lab
```

## Alternative: Docker Environment

[![Docker logo](https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png){ width="100" }](https://www.docker.com/)

If you prefer to use Docker instead of a local installation:

1. [Install Docker](https://docs.docker.com/get-docker/)
2. Build and run from the repository root:

```bash
docker build -t reproducible/base -f environment/docker/Dockerfile .
docker run -it --rm -v "$PWD":/home/repro reproducible/base bash
```

## Alternative: Dev Container

If you use VS Code, you can open the repository in a
[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)
for a fully configured environment. Just open the repository folder and
VS Code will prompt you to reopen in the container.
