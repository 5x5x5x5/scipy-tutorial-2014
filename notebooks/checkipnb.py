#!/usr/bin/env python
"""Run notebooks and report exceptions.

Usage: python checkipnb.py foo.ipynb [bar.ipynb [...]]

Each cell is executed and checked for errors.
This is a modernized version of the original script, updated
to use the current nbformat and jupyter_client APIs.

For CI, consider using pytest with nbval instead:
    pytest --nbval notebooks/
"""

import sys

import nbformat
from jupyter_client.manager import KernelManager


def run_notebook(nb):
    km = KernelManager(kernel_name="python3")
    km.start_kernel()
    kc = km.client()
    kc.start_channels()
    kc.wait_for_ready()

    cells = 0
    failures = 0
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        kc.execute(cell.source)
        reply = kc.get_shell_msg(timeout=60)["content"]
        if reply["status"] == "error":
            failures += 1
            print("\nFAILURE:")
            print(cell.source)
            print("-----")
            print("raised:")
            print("\n".join(reply["traceback"]))
        cells += 1
        sys.stdout.write(".")

    print()
    print("ran notebook %s" % nb.metadata.get("title", "(untitled)"))
    print("    ran %3i cells" % cells)
    if failures:
        print("    %3i cells raised exceptions" % failures)
    kc.stop_channels()
    km.shutdown_kernel()


if __name__ == "__main__":
    for ipynb in sys.argv[1:]:
        print("running %s" % ipynb)
        with open(ipynb) as f:
            nb = nbformat.read(f, as_version=4)
        run_notebook(nb)
