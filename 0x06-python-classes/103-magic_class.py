#!/usr/bin/python3
""" Magic Class module"""
import math


class MagicClass:
    """Circle Class"""
    def __init__(self, radius=0):
        """Initialize the circle"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate circumference of the circle"""
        return 2 * math.pi * self.__radius
