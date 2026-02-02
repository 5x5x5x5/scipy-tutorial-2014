"""EyeSize test with origin-based naming for inputs and outputs."""

import os
import shutil
import sys

sys.path.append("..")

import SimpleITK as sitk

import eyesize
import imagedownloader


def test_eyesize_withorigin():
    downloader = imagedownloader.ImageDownloader()
    estimator = eyesize.EyeSize()

    figshare_id = "1066744"
    seed_points = [204, 400]
    expected_output_radius_estimate = 85

    input_name = f"TralitusSaltrator_figshare_{figshare_id}.jpg"
    output_name = f"SegmentedEye_{seed_points[0]}_{seed_points[1]}.png"

    inputs_dir = os.path.join(os.getcwd(), "inputs")
    outputs_dir = os.path.join(os.getcwd(), "outputs")

    input_path = os.path.join(inputs_dir, input_name)
    output_path = os.path.join(outputs_dir, output_name)

    # Clear inputs folder
    if os.path.isdir(inputs_dir):
        shutil.rmtree(inputs_dir)
    os.mkdir(inputs_dir)

    # Clear outputs folder
    if os.path.isdir(outputs_dir):
        shutil.rmtree(outputs_dir)
    os.mkdir(outputs_dir)

    downloader.set_figshare_id(figshare_id)
    downloader.set_image_name(input_path)
    downloader.download()

    input_image = sitk.ReadImage(input_path)

    estimator.set_image(input_image)
    estimator.set_seed_point(seed_points)

    eyes_segmented, radius_estimate = estimator.estimate()

    sitk.WriteImage(eyes_segmented, output_path)

    assert radius_estimate == expected_output_radius_estimate, (
        f"Problem with estimating radius: current: {radius_estimate}, "
        f"expected: {expected_output_radius_estimate}"
    )
