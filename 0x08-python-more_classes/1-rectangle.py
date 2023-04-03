#!/usr/bin/python3

"""
    Defines a rectangle with width and height
"""


class Rectangle:
    """A class that represents rectangle"""
    def __init__(self, width=0, height=0):
        """ Initializes the classes with the given value
            Args:
                width: the width of the rectangle
                height: the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("eight must be an integer")
        if value < 0:
            raise ValueError("eight must be >= 0")
        self.__height = value
