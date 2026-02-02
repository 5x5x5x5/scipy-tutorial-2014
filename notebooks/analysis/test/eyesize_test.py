import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import eyesize
import imagedownloader
import SimpleITK as sitk


def test_eye_radius_estimation():
    """Download a test image from Figshare and verify the eye radius estimate."""
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

    sitk.WriteImage(eyes_segmented, "SegmentedEye.png")

    assert radius_estimate == 8.5
