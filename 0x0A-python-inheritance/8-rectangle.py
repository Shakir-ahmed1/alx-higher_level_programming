#!/usr/bin/python3
""" a module with BaseGeometry calss"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle a geometry with 4 sides """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
