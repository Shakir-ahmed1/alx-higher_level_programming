#!/usr/bin/python3
"""Write a function that adds a new attribute to an object if it’s possibl
"""


def add_attribute(obj, attr, val):
    """ adds an attribute to an object at runtime """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribute")
