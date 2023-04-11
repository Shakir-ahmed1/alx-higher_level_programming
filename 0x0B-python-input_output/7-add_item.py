#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python list, and then save
them to a file:
"""
from sys import argv
from os.path import exists
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if not exists("add_item.json"):
    a = []
else:
    a = load_from_json_file("add_item.json")

for b in range(1, len(argv)):
    a.append(argv[b])
save_to_json_file(a, "add_item.json")
