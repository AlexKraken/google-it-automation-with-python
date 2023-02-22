#!/usr/bin/env python3
"""
This script resizes, rotates and converts images into jpgs.

Suggested Usage: make it an excutable script (e.g. chmod +x)
and run from the command line with the source folder and destination folder
as command line arguments

./image-fixer.py <source directory> <destination directory>
./image-fixer.py images /opt/icons
"""
import os, sys, glob
from PIL import Image

new_size = (128, 128)
degrees = 90
source = glob.glob(sys.argv[1] + r"/*")
destination = sys.argv[2]

for input_image in source:
    head, tail = os.path.split(input_image)
    filename, ext = os.path.splitext(tail)
    output_image = destination + r"/" + filename + ".jpg"

    if input_image != output_image:
        try:
            with Image.open(input_image) as image:
                image.convert("RGB").resize(new_size).rotate(degrees).save(output_image)
        except OSError:
            print("Cannot convert", input_image)
