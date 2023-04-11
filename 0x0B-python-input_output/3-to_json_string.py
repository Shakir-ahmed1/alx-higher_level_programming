#!/usr/bin/python3
"""
Write a function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """ serializes the object to json formated string"""
    return json.dumps(my_obj)
