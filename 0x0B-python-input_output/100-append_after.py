#!/usr/bin/python3
"""Write a function that inserts a line of text to a file, after
each line containing a specific string"""


def append_after(filename='', search_string="", new_string=""):
    """ inserts the given new_string after each line search_string appears"""
    with open(filename, mode="r") as f:
        ls = f.readlines()
        result = []
        for a in ls:
            result.append(a)
            if search_string in a:
                result.append(new_string)
    with open(filename, mode="w") as f:
        f.write("".join(result))
