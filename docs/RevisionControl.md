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

### Clone a Repo

```bash
git clone https://github.com/your-username/scipy-tutorial-2014.git
```

### Create a Branch

```bash
git checkout -b my-working-branch
```

This creates a branch *from* whatever branch is currently checked out. It is
typically best to branch from main only, unless there is a reason to branch
from an existing branch.

### Make a Commit

```bash
git add -u                           # stages all changed files, including deleted files
git commit -m "Briefly describe your changes"  # Try for 50 characters or less
```

### See Your Changes

```bash
git log main..
git diff main...
```

### Push Your Branch

```bash
git push -u origin my-working-branch
```

When you are ready, create a pull request on GitHub to merge your work.

### Seeing Changes in Main

If your pull request was not from a fork, the changes you made will be
available on the main branch.

```bash
git pull origin main
git log main
git log main --first-parent
```

### Working with Forks

If your pull request was from a fork, you will need to pull changes from the
upstream repository to get your changes in main.

```bash
git remote -v   # list remotes
git remote add upstream https://github.com/reproducible-research/scipy-tutorial-2014
git remote -v   # should now see your new upstream remote
```

To update your fork from upstream:

```bash
git fetch upstream
git rebase upstream/main
```

Then push those changes back up to your fork on GitHub:

```bash
git push origin main
```

### Create a Citable Version

GitHub integrates with [Zenodo](https://zenodo.org) to assign DOIs to releases.
To make your code citable:

1. Link your GitHub repository to Zenodo at [zenodo.org/account/settings/github](https://zenodo.org/account/settings/github/)
2. Create a GitHub release
3. Zenodo automatically archives it and assigns a DOI

See the [GitHub guide on making code citable](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).

## Resources

* [GitHub Flow](https://guides.github.com/introduction/flow/)
* [Making code citable](https://guides.github.com/activities/citable-code/)
