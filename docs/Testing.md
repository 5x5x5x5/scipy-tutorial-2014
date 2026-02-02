# Testing

## Why Test?

Testing code is the scientific method applied to software development:

* **Hypothesis**: Your code does X
* **Experiment**: Run the test
* **Observation**: Did it actually do X?

Without tests, you cannot verify that your analysis pipeline produces correct
results. Tests are especially important when refactoring or updating
dependencies.

## pytest

This project uses [pytest](https://docs.pytest.org/) for testing.

Run the test suite:

```bash
uv run pytest
```

### Example Test

The `test/eyesize_test.py` file contains an integration test that:

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

    assert radius_estimate == 8.5
```

## Continuous Integration

The repository includes a GitHub Actions workflow (`.github/workflows/ci.yml`)
that automatically runs tests on every push and pull request. This ensures that
changes don't break existing functionality.

## Hands On

1. Run the test suite: `uv run pytest`
2. Look at `test/eyesize_test.py` to understand how the test works
3. Add a test for the `overlay_segmentation` function in `dexy/eyesize.py`
4. Run the tests again and verify your new test passes
