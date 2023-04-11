#!/usr/bin/python3
""" Write a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """ reads and prints a utf-8 file content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
