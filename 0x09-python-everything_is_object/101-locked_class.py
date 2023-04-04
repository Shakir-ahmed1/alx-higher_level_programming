#!/usr/bin/python3
"""a module that have a function to lock a new instance creation"""


class LockedClass:
    """Lockes a class from creating a new instance"""
    __slots__ = ["first_name"]
