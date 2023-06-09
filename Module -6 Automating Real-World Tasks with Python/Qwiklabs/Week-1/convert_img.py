#!/usr/bin/env python3

from PIL import Image
import os

source_dir = os.path.expanduser("~") + "/images/"
destination_dir = "/opt/icons/"

for image in os.listdir(source_dir):
    if "." not in image[0]:
        new_image = Image.open(source_dir + image)

        new_image.rotate(270).resize((128, 128)).convert("RGB").save(
            destination_dir + image.split(".")[0], "jpeg")
        new_image.close()
