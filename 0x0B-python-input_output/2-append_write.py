#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """ appends a text to a file"""
    with open(filename, encoding="utf-8", mode="a") as f:
        return f.write(text)
