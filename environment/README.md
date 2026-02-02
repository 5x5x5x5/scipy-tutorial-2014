# Computational Environment Setup

## Recommended: uv

The simplest way to set up the environment is with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
uv run python check_env.py
```

## Alternative: Docker

See the [docker/](docker/) directory for Docker-based setup.

## Validation

Run the [check_env.py](check_env.py) script to validate your environment:

```bash
uv run python environment/check_env.py
```
