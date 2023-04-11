#!/usr/bin/python3
"""Write a function that adds a new attribute to an object if it’s possibl
"""


def add_attribute(obj, attr, value):
    """ adds a new attribute if it is possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new add new attribute")
    setattr(obj, attr, value)
