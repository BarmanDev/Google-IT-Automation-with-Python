#!/usr/bin/env python3
import os
import requests

dir_path = "/data/feedback/"
folder = os.listdir(dir_path)

list = []

for feedback in folder:
    with open(dir_path + feedback, "r") as file:

        list.append({"title": file.readline().rstrip("\n"),
                     "name": file.readline().rstrip("\n"),
                     "date": file.readline().rstrip("\n"),
                     "feedback": file.read().rstrip("\n")})

for item in list:
    resp = requests.post("http://0.0.0.0/feedback/", json=item)
    if resp.status_code != 201:
        raise Exception(
            "Post failed with error status code {}".format(resp.status_code))
    print("Added feedback ID: {}".format(resp.json()["id"]))
