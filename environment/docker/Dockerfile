# Dockerfile for the Reproducible Research tutorial
#
#  Reproducible Research: Walking the Walk
#
FROM python:3.13-slim-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create non-root user
RUN useradd -m repro
ENV HOME=/home/repro
USER repro
WORKDIR /home/repro

# Copy project files and install dependencies
COPY --chown=repro:repro pyproject.toml .python-version ./
RUN uv sync --no-dev

COPY --chown=repro:repro . .
