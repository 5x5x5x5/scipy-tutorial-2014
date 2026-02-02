# -*- coding: utf-8 -*-

from urllib.request import urlopen, urlretrieve
import json


class ImageDownloader:

    def __init__(self, figshare_id=None, image_name=None):
        self.figshare_id = figshare_id
        self.image_name = image_name

    def set_figshare_id(self, figshare_id):
        self.figshare_id = figshare_id

    def set_image_name(self, image_name):
        self.image_name = image_name

    def download(self):
        figshare_url = "https://api.figshare.com/v2/articles/%s" % self.figshare_id
        response = urlopen(figshare_url)
        info = json.loads(response.read().decode("utf-8"))
        image_url = info["files"][0]["download_url"]
        urlretrieve(image_url, self.image_name)
