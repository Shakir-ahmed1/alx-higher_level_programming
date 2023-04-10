#!/usr/bin/python3
""" Only sub class of"""


def inherits_from(obj, a_class):
    """ checks if the given object has inheritance with the class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
