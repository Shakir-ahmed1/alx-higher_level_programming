#!/usr/bin/python3
""" a module that prints list of attributes of an object"""

def lookup(obj):
    """Returns a list of attributes of the given object"""
    return dir(obj)
