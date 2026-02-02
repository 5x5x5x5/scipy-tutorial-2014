# Docker Compute Environment

In this hands-on exercise, we will learn how to create and use a reproducible
computational environment with Docker.

## Installing Docker

You must already have [Docker](https://www.docker.com/) installed. See the
[Docker installation documentation](https://docs.docker.com/get-docker/) for
more information.

On Linux, install Docker Engine. On Mac or Windows, install
[Docker Desktop](https://www.docker.com/products/docker-desktop/).

## Build the Docker Base Image

We need to build the Docker *images*, our reproducible computational
environments. Docker images are built from a set of instructions in a
[Dockerfile](https://docs.docker.com/reference/dockerfile/).

From the repository root directory, build the base image:

```bash
docker build -t reproducible/base -f environment/docker/Dockerfile .
```

## Running Docker

To launch the base image and open a shell:

```bash
docker run -it --rm -v "$PWD":/home/repro reproducible/base bash
```

You are now in a Docker *container*. The `-it` flags tell Docker to start up a
pseudo-terminal and keep stdin open. Enter `exit` to exit the shell.

## JupyterLab Container

Build and run the JupyterLab image:

```bash
docker build -t reproducible/jupyter -f environment/docker/Dockerfile-ipython .
docker run -d -p 8888:8888 -v "$PWD/notebooks":/home/repro/notebooks --name jupyter reproducible/jupyter
```

Then point your browser to `http://localhost:8888`.

To stop and remove the container:

```bash
docker stop jupyter
docker rm jupyter
```

## Documentation Build Container

Build and run the docs image:

```bash
docker build -t reproducible/docs -f environment/docker/Dockerfile-dexy .
docker run --rm -v "$PWD":/home/repro reproducible/docs
```

The generated site will be in the `site/` directory.

## Docker Help

For a full list of Docker commands, enter `docker` with no arguments. For help
on a specific subcommand, use `docker <subcommand> --help`.
