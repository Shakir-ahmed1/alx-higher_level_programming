#!/usr/bin/python3
""" a module with BaseGeometry calss"""


class BaseGeometry:
    """ A class with unimplimentd area"""
    def area(self):
        """ An area with no implimentstion"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates integers for latter use"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
