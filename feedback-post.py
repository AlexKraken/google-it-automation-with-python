#! /usr/bin/env python3
"""
This script takes reviews (saved as individual .txt files) and POSTs them to a
website (using Django) 

Suggested Usage: make it an excutable script (e.g. chmod +x) and run from the 
command line

./feedback-post.py
"""
import os
import requests


website = r"http://<server ip address>/feedback/"

path = r"/data/feedback"
directory_list = os.listdir(path)


def parse_feedback(filename: str) -> dict:
    """This function takes in the full path of a text file containing feedback
    and returns a dictionary of the information.
    """
    feedback = {}
    with open(filename) as file:
        feedback.update({"title": file.readline()})
        feedback.update({"name": file.readline()})
        feedback.update({"date": file.readline()})
        feedback.update({"feedback": file.readline()})

    return feedback


print(f"Files and directories in {path}:")
print(directory_list)

for file in directory_list:
    if os.path.splitext(file)[1] == ".txt":
        file_path = os.path.join(path, file)
        feedback = parse_feedback(file_path)
        response = requests.post(website, data=feedback)

        print(f"{file} result: {response.status_code}")
