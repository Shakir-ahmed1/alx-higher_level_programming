#!/usr/bin/python3
"""
Write a function that gets the JSON representation of an object (string)
and save it to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """ serializes the object to json formated string and saves it to file"""
    with open(filename, encoding="utf-8", mode="w") as f:
        json.dump(my_obj, f)
