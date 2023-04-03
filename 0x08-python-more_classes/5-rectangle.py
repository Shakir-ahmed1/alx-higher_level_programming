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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
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
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """The perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """prints the rectangle using # """
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for a in range(self.__height):
            result += "#" * self.__width
            if a != self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """returns the string that enables to recreate same rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """notifies at deletion of the rectangle"""
        print("Bye rectangle...")
