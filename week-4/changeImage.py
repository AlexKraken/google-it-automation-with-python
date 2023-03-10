#!/usr/bin/env python3

import os
from PIL import Image

# Directory containing the original images
source = r"supplier-data/images/"

# Original image file is a 3000x2000 .TIFF (RGBA)
# Convert to 600x400 .JPEG (RGB)
new_size = (600, 400)

for filename in os.listdir(source):
    root, extension = os.path.splitext(filename)
    input_image = os.path.join(source, filename)
    output_image = os.path.join(source, root + ".jpeg")

    if input_image != output_image:
        try:
            with Image.open(input_image) as image:
                image.convert("RGB").resize(new_size).save(output_image)
        except OSError:
            print("Cannot convert", input_image)
