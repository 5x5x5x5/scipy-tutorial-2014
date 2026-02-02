# Revision Control

## Why Version Control?

Version control tracks changes to your code, data, and documentation over time.
It is essential for reproducible research because it:

* Records the exact state of your project at any point in time
* Enables collaboration without overwriting each other's work
* Provides unique hashes for every change, making it citable and verifiable
* Allows branching and merging for parallel experiments

## Git and GitHub

[Git](https://git-scm.com) is the most widely used version control system.
[GitHub](https://github.com) hosts Git repositories and provides collaboration
tools (pull requests, issues, CI/CD).

## Hands On

### Create a Branch

```bash
git checkout -b my-analysis
```

### Make a Commit

```bash
git add notebooks/03-DataProcessing.ipynb
git commit -m "Add analysis of acquired microscopy images"
```

### Push the Branch

```bash
git push -u origin my-analysis
```

### Create a Citable Version

GitHub integrates with [Zenodo](https://zenodo.org) to assign DOIs to releases.
To make your code citable:

1. Link your GitHub repository to Zenodo at [zenodo.org/account/settings/github](https://zenodo.org/account/settings/github/)
2. Create a GitHub release
3. Zenodo automatically archives it and assigns a DOI

See the [GitHub guide on making code citable](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).
