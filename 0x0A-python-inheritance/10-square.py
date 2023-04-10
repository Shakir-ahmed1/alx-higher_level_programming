#!/usr/bin/python3
""" a module with BaseGeometry calss"""


class BaseGeometry:
    """ A class with unimplimentd area"""
    def area(self):
        """ An area with no implimentstion"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates integers for latter use"""
        if not isinstance(value, int) or type(value) == bool:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle a geometry with 4 sides """
    def __init__(self, width, height):
        """ Initializes width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Area of the rectangle """
        return self.__height * self.__width

    def __str__(self):
        """ The string representation of the rectangle class """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ Square a rectangle with same width and height"""
    def __init__(self, size):
        """ Initializes the size of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ calculates the area of the square"""
        return self.__size ** 2
