# Agenda

## First Session

### Getting Started

* Get acquainted and verify preparations (5 min)
    * Say *Hi!* to the instructors
    * Introduce yourself to the person sitting next to you, they will be your
  partner
    * Recall successfully completing the [preparation](Preparation.md) tasks

### Introduction

History and Motivation for Reproducible Research (10 min)

* History of scientific societies and publications
    * [Leeuwenhoek](https://en.wikipedia.org/wiki/Antonie_van_Leeuwenhoek) was The Man!
    * [The Invisible College](https://en.wikipedia.org/wiki/Invisible_College)
    * [Nullius in Verba](https://royalsociety.org/about-us/history/)

### Data Acquisition

[Image Acquisition](DataAcquisition.md) (25 min)

* Replication of the early microscope experiments by Antonie Leeuwenhoek
    * Cell camera phone microscope
    * With drop of interesting water
    * *Hands on:* each pair acquires images

### Data Sharing

[Data Sharing](DataSharing.md) (20 min)

* Image gathering, storage, and sharing (10 min)
    * [Figshare](https://figshare.com)
    * *Hands on:* Upload the images
* Download data via RESTful API (10 min)
    * REST download via Python standard library
    * Checksum verification
    * *Hands on:* Download the data via HTTP

## Second Session

### Reproducible Computational Environment

[Computational Environment](ComputationalEnvironment.md) (20 min)

* Reproducible computational environment
    * Docker
    * `uv` and `pyproject.toml` for dependency management
    * Dev Containers
* *Hands on:*
    * Set up the environment using `uv sync`
    * Run the environment verification script
    * Build a Docker image

### Developing Reproducible Scripts and Modules

[JupyterLab, Scripts, and SimpleITK](DataProcessing.md) (20 min)

* Reproducible code development
    * JupyterLab to combine notes, code, and results
    * Avoid duplication with re-usable modules
* *Hands on:*
    * Run analysis on new data
    * Generate histogram for the data

### Revision Control

[Revision Control](RevisionControl.md) with Git and GitHub (20 min)

* Software versioning, collaboration, and citation
    * Keeping track of changes
    * Unique hashes
    * DOI
* *Hands on:*
    * Create a branch
    * Make a commit
    * Push the branch
    * Create a citable version

## Break (15 min)

## Third Session

### Regression Testing

[Testing](Testing.md) (30 min)

* Quality code development with regression tests
    * Testing code hypothesis: the scientific method applied to development
    * Unit testing with pytest
    * Integration testing
    * Continuous integration with GitHub Actions
* *Hands on:*
    * Run the test suite with `uv run pytest`
    * Add coverage for another method to the unit tests

### Literate Programming

[Literate Programming](LiterateProgramming.md) (30 min)

* Document generation with MkDocs
* Markdown documentation
* GitHub Pages deployment
* *Hands on:* build the documentation site with `uv run mkdocs build`

## Fourth Session

### Open Science Publication

Submitting an article to a Reproducible Journal (20 min)

* Open Science Publication
    * Open Access
    * Publishes article, data, and code
* *Hands on:*
    * Submit Article to the Insight Journal
    * Point to GitHub fork for source code

### Replicate or Perish!

Attempt to replicate your peers' articles (40 min)

* Replicate the publications of groups next to you
* Share your observations
