#! /usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
source = r"supplier-data/images"

for filename in os.listdir(source):
    name, extension = os.path.splitext(filename)
    
    if extension == ".jpeg":
        path = os.path.join(source, filename)
        with open(path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
