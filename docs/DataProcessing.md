# Data Processing

Now that we have data in online sharing sites, we can start processing it.
When processing, we want to keep the following best practices in mind:

* Avoid duplication of code: maximize re-use
* Keep track of the full state with version identifiers
* Make sure all analysis is tested
* Data, code, and documentation are coupled

The latter three topics are covered in further detail in the upcoming
sessions on revision control, regression testing, and literate programming.


## JupyterLab

[![Jupyter](https://jupyter.org/assets/logos/rectanglelogo-greytext-orangebody-greymoons.svg){ width="200" }](https://jupyter.org/)

[JupyterLab](https://jupyterlab.readthedocs.io/) is one of the best existing
resources for reproducible research practices.

* Learn it!
* Love it!

Launch it with:

```bash
uv run jupyter lab
```

When it becomes desirable to re-use code outside of the notebook, it is helpful
to incrementally refactor by creating classes or functions. These classes or
functions can be stored in Python modules and imported into the notebook.

!!! warning "Avoid Copy-Paste"
    Never duplicate code between notebooks and scripts. Put reusable logic
    in modules (like `notebooks/analysis/eyesize.py`) and import them.

There is a helpful IPython magic for this type of rapid development. The
`autoreload` extension automatically re-imports modules when they change on
disk:

```python
%load_ext autoreload
%autoreload 2
```

This way, you can edit your module in a text editor and immediately use
the updated code in the notebook without restarting the kernel.

## Hands On

Run through the [03-DataProcessing.ipynb](https://nbviewer.org/github/reproducible-research/scipy-tutorial-2014/blob/master/notebooks/03-DataProcessing.ipynb) notebook in the repository. At the
end of the notebook, there is a simple exercise on code re-use. Explore
analysis on your images or images of nearby groups. Save the updated notebook
to disk.
