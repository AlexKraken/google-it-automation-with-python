#! /usr/bin/env python3

import os
import requests

source = r"supplier-data/descriptions"
website = r"http://<server>/fruits/"
fruit_data = {}

for filename in os.listdir(source):
    name, extension = os.path.splitext(filename)
    print(filename, extension)
    if extension == ".txt":
        with open(os.path.join(source, filename)) as input_file:
            fruit_name = input_file.readline().strip()
            fruit_weight = int(input_file.readline().split()[0])
            fruit_description = input_file.readline()

            fruit_data.update({"name": fruit_name, 
                               "weight": fruit_weight,
                               "description": fruit_description,
                               "image_name": name + ".jpeg"})
            response = requests.post(website, data=fruit_data)
            print(f"{fruit_name} result: {response.status_code}")

