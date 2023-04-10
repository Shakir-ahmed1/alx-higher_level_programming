#!/usr/bin/python3
""" module for instance vs class checker """


def is_same_class(obj, a_class):
    """ checkes if the given object is an instance of the class"""
    return type(obj) == a_class
