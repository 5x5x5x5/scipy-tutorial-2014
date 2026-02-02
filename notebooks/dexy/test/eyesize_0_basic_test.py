"""Basic EyeSize test - downloads image and verifies radius estimate."""

import sys

sys.path.append("..")

import SimpleITK as sitk

import eyesize
import imagedownloader


def test_eyesize_basic():
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

    assert radius_estimate == 85
