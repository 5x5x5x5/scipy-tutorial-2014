# Computational Environment

Even though computers are often considered deterministic, computational
software is a rapidly evolving and changing landscape. Libraries are constantly
adding new features and fixing issues. As computer hardware evolves, software
is forced to adapt accordingly.

A reproducible computational environment is sufficiently consistent for the
computational task at hand. For example, this can consist of a similar CPU
instruction set, libraries and executables with a specific version
and configuration options, a specific operating system version, etc.

## uv and pyproject.toml

The simplest way to manage a reproducible Python environment is with
[uv](https://docs.astral.sh/uv/) and a `pyproject.toml` file.

`pyproject.toml` declares all project dependencies with version constraints.
`uv.lock` pins exact versions for fully reproducible installs. Running
`uv sync` installs the exact same environment everywhere.

```bash
# Install all dependencies
uv sync

# Run any command in the project environment
uv run python my_script.py
uv run pytest
uv run jupyter lab
```

!!! tip "Why uv?"
    [uv](https://docs.astral.sh/uv/) is an extremely fast Python package and
    project manager written in Rust. It replaces pip, virtualenv, pyenv, and
    more with a single tool. It is developed by [Astral](https://astral.sh/),
    the creators of the [Ruff](https://docs.astral.sh/ruff/) linter.

## Docker

![Docker filesystems](https://tiewei.github.io/images/docker-filesystems-multilayer.png){ width="350" align="right" }

[Docker](https://www.docker.com/) is an open-source engine that automates the
deployment of any application as a lightweight, portable, self-sufficient
container that will run virtually anywhere.

Docker works with images that consume minimal disk space, are versioned,
archiveable, and shareable. Executing applications in these images does not
require dedicated resources and is high performance.

![Container vs VMs](https://tiewei.github.io/images/docker_vm.jpg){ width="350" }

For more information on Docker, visit the [Docker documentation](https://docs.docker.com/get-started/).

The tutorial includes a `Dockerfile` at `environment/docker/Dockerfile` that
builds a complete environment:

```bash
# Build the image
docker build -t reproducible/base -f environment/docker/Dockerfile .

# Run an interactive shell
docker run -it --rm -v "$PWD":/home/repro reproducible/base bash

# Run JupyterLab
docker build -t reproducible/jupyter -f environment/docker/ipython/Dockerfile .
docker run -d -p 8888:8888 --name jupyter reproducible/jupyter
```

## Dev Containers

[Dev Containers](https://containers.dev/) integrate Docker with your IDE. The
tutorial includes a `.devcontainer/devcontainer.json` configuration that works
with:

* **VS Code** - Open the folder and accept the "Reopen in Container" prompt
* **GitHub Codespaces** - Click "Open in Codespaces" on the repository page

The dev container automatically installs uv and runs `uv sync` on creation.

## Virtual Machines

As the name suggests, a Virtual Machine (VM) emulates a physical computer. In
the last few years, VMs have become very popular because of their scalability,
ease of maintenance, and reproducibility. Docker containers are generally
preferred for development environments because they're lighter-weight, but VMs
are still useful for:

* Accurately modeling a multi-server production topology
* Testing on different operating systems
* Disaster-case testing: machines dying, network partitions, slow networks

## Package Managers and Distributions

Part of the problem in creating a computational environment is the procurement
of necessary libraries and other dependencies.

* **Python**: [uv](https://docs.astral.sh/uv/) (recommended), pip, conda
* **Linux**: apt (Debian/Ubuntu), dnf/yum (Fedora/RHEL), pacman (Arch)
* **macOS**: [Homebrew](https://brew.sh/)
* **Windows**: [winget](https://learn.microsoft.com/en-us/windows/package-manager/), [Chocolatey](https://chocolatey.org/)

Scientific Python distributions like [Anaconda](https://www.anaconda.com/download)
are also available.

## Hands-On

1. Set up your environment with `uv sync`
2. Run `uv run python environment/check_env.py` to validate
3. (Optional) Build the Docker image and verify it works
4. (Optional) Upload your Docker image to [DockerHub](https://hub.docker.com)
