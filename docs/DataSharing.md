# Data Sharing

## Introduction

### Data Items as Papers

In the new environment of modern scientific publishing, data items are finally
getting the equivalent status of papers. We can today publish a dataset and get
a Digital Object Identifier
([DOI](https://en.wikipedia.org/wiki/Digital_object_identifier)) reference to it,
making it citable.

For example:

> Ortega, Ana; Behdadfar, Sareh; Li, Lin; Zenteno, Omar (2014):
> Tralitus Saltator. figshare.
> [https://doi.org/10.6084/m9.figshare.1066744](https://doi.org/10.6084/m9.figshare.1066744)

### Career Rewards

Now that data items are citable, data sharing activities can be accounted as
part of the career reward system for researchers. Thus recognizing the valuable
contributions that data sharers make to their respective fields and communities.

In this new environment, data items no longer need to be sequestered until a
traditional article is published. Instead, data can be shared immediately after
acquisition for the benefit of the larger scientific community.

### Data Sharing Sites

Many data sharing sites are available. Here are a few examples:

* [Figshare](https://figshare.com)
* [Zenodo](https://zenodo.org)
* [Dryad](https://datadryad.org)

You may find additional specific data sharing sites for your specific field.

## Hands-On

Now that we have acquired several images in the mobile device, it is time to
move these images to an online platform where they can be cataloged, linked to,
and downloaded.

Here we are going to perform this in three steps:

* Export images from the mobile device
* Upload images to a data sharing web site
* Download images via REST API

## Exporting Images

There are many options for exporting images from your mobile device (phone or
tablet). Typical options include:

* **Cloud sync** (iCloud, Google Photos, etc.) - usually the most convenient
* **Email** - send the image to yourself
* **Direct transfer** - USB cable, AirDrop, or similar

## Sharing Images

Now that you have brought the images to your local machine, you can upload them
to your data sharing account. Here we focus on using Figshare.

### Figshare

1. Log in to your [Figshare account](https://figshare.com/account/my_data)
2. Click on "Upload" to add your image
3. Fill in the metadata:
    * Select a title for the image (use a serious and descriptive title)
    * Select a Category from the dropdown menu (e.g., "Biological Techniques")
    * Enter a serious description in the "Description" field
4. Click "Publish" to make the image publicly available
5. The image will receive a DOI for permanent citation

### Finding the Article ID

For a given image, take note of its identifier. For example, the URL
`https://figshare.com/articles/Tardigrades_Image_01/1050595` has the identifier
`1050595`.

### Downloading via API

Use the identifier with the [Figshare API v2](https://docs.figshare.com/):

```
https://api.figshare.com/v2/articles/1050595
```

This returns a JSON structure containing the article metadata, including a
`files` array with `download_url` entries for each file.

See the `02-DataSharing.ipynb` notebook for a hands-on example of downloading
data programmatically with Python's `urllib`.

## Hands On

* Repeat this process with your image in Figshare
* Use the `02-DataSharing.ipynb` notebook to download it via the API
* Verify that the file appears in your file system
