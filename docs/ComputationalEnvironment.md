# Computational Environment

A reproducible computational environment ensures that anyone can recreate your
exact analysis setup. This is critical for verification and collaboration.

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

[Docker](https://www.docker.com/) packages an entire operating system
environment into a portable container. Containers are more lightweight than
virtual machines -- they share the host kernel and start in milliseconds.

The tutorial includes a `Dockerfile` at `environment/docker/Dockerfile` that
builds a complete environment:

```bash
# Build the image
docker build -t reproducible/base -f environment/docker/Dockerfile .

# Run an interactive shell
docker run -it --rm -v "$PWD":/home/repro reproducible/base bash

# Run JupyterLab
docker build -t reproducible/jupyter -f environment/docker/Dockerfile-ipython .
docker run -d -p 8888:8888 --name jupyter reproducible/jupyter
```

## Dev Containers

[Dev Containers](https://containers.dev/) integrate Docker with your IDE. The
tutorial includes a `.devcontainer/devcontainer.json` configuration that works
with:

* **VS Code** - Open the folder and accept the "Reopen in Container" prompt
* **GitHub Codespaces** - Click "Open in Codespaces" on the repository page

The dev container automatically installs uv and runs `uv sync` on creation.

## Exercise

1. Set up your environment with `uv sync`
2. Run `uv run python environment/check_env.py` to validate
3. (Optional) Build the Docker image and verify it works
