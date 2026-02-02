#!/usr/bin/env python
"""Computational environment validation script for the Reproducible Research tutorial.

https://github.com/reproducible-research/scipy-tutorial-2014
"""

import subprocess
import sys


def main():
    return_value = 0

    required_packages = ["numpy", "scipy", "matplotlib", "SimpleITK"]
    for package in required_packages:
        print("Importing " + package + " ...")
        try:
            __import__(package, globals(), locals(), [], 0)
        except ImportError:
            print("Error: could not import " + package)
            return_value += 1

    print("")
    required_executables = ["git", "jupyter", "pytest"]
    for executable in required_executables:
        print("Checking for " + executable + " ...")
        try:
            process = subprocess.Popen(
                [executable, "--help"],
                stderr=subprocess.STDOUT,
                stdout=subprocess.PIPE,
            )
            process.wait()
        except OSError:
            print("Error: could not execute " + executable)
            return_value += 1

    if return_value == 0:
        print("\nSuccess. All dependencies are available.")
    else:
        print(
            "\nA defect was found in your environment, please see the messages above."
        )
    sys.exit(return_value)


if __name__ == "__main__":
    main()
