#!/usr/bin/python3
"""A module that adds two integers"""


def add_integer(a, b=98):
    """Adds two integers"""
    if not(type(a) in [float, int]):
        raise TypeError("a must be an integer")
    if not(type(b) in [float, int]):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
