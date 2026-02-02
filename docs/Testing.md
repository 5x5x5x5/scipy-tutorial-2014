# Testing

## Why Test?

Testing code is the scientific method applied to software development:

* **Hypothesis**: Your code does X
* **Experiment**: Run the test
* **Observation**: Did it actually do X?

Without tests, you cannot verify that your analysis pipeline produces correct
results. Tests are especially important when refactoring or updating
dependencies.

## Unit Tests

To ensure that improvements made to your code or updates in the computing
environment are not changing the expected results of each module, we write
[unit tests](https://en.wikipedia.org/wiki/Unit_testing#Benefits).

More details:

* [Python unittest documentation](https://docs.python.org/3/library/unittest.html)
* [Testing Your Code - The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/tests/)

## Integration Testing

[Integration testing](https://en.wikipedia.org/wiki/Integration_testing)
consists of writing tests that check that all your modules can work together.

## pytest

This project uses [pytest](https://docs.pytest.org/) for testing.

Run the test suite:

```bash
uv run pytest
```

### Example Test

The `notebooks/analysis/test/eyesize_test.py` file contains an integration test that:

1. Downloads a test image from Figshare
2. Runs the eye segmentation algorithm
3. Asserts the estimated radius matches the expected value

```python
def test_eye_radius_estimation():
    downloader = imagedownloader.ImageDownloader()
    estimator = eyesize.EyeSize()

    image_name = "TralitusSaltrator.jpg"

    downloader.set_figshare_id("1066744")
    downloader.set_image_name(image_name)
    downloader.download()

    input_image = sitk.ReadImage(image_name)

    estimator.set_image(input_image)
    estimator.set_seed_point([204, 400])

    eyes_segmented, radius_estimate = estimator.estimate()

    assert radius_estimate == 85
```

### Progressive Test Improvement

The `notebooks/analysis/test/` directory contains a series of test files that
demonstrate how to progressively improve your tests:

1. **eyesize_0_basic_test.py** - Basic test: download, process, assert
2. **eyesize_1_noisy_test.py** - Add informative error messages to assertions
3. **eyesize_2_cleanplate_test.py** - Use clean input/output directories
4. **eyesize_3_withorigin_test.py** - Include data provenance in file names

## Continuous Integration

The repository includes a GitHub Actions workflow (`.github/workflows/ci.yml`)
that automatically runs tests on every push and pull request. This ensures that
changes don't break existing functionality.

## Hands On

1. Run the test suite: `uv run pytest`
2. Look at `notebooks/analysis/test/eyesize_test.py` to understand the basic test
3. Work through the [04-RegressionTesting notebook](../notebooks/04-RegressionTesting.ipynb)
   to see how tests evolve from basic to robust
4. Add a test for the `overlay_segmentation` function in `notebooks/analysis/eyesize.py`
5. Run the tests again and verify your new test passes
