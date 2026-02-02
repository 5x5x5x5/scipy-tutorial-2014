#!/bin/sh
set -e

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

### "build-reproducible"
docker build -t reproducible/base -f environment/docker/Dockerfile "$REPO_ROOT"

### "build-docs"
docker build -t reproducible/docs -f environment/docker/Dockerfile-dexy "$REPO_ROOT"

### "build-jupyter"
docker build -t reproducible/jupyter -f environment/docker/Dockerfile-ipython "$REPO_ROOT"

### "run-docs"
docker run --rm -v "$REPO_ROOT":/home/repro reproducible/docs

### "start-jupyter"
docker run -d -p 8888:8888 -v "$REPO_ROOT/notebooks":/home/repro/notebooks --name jupyter reproducible/jupyter

### "jupyter-ps"
docker ps
docker port jupyter 8888

### "jupyter-stop"
docker stop jupyter
docker rm jupyter
