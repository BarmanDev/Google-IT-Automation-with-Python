#!/usr/bin/env python3

import os
from PIL import Image

dir_path = os.path.expanduser("~") + "/supplier-data/images/"

for image in os.listdir(dir_path):
    if ".tiff" in image and "." not in image[0]:
        img = Image.open(dir_path + image).convert("RGB")
        img.resize((600, 400)).save(
            dir_path + image.split(".")[0] + ".jpeg", "jpeg")
        img.close()
