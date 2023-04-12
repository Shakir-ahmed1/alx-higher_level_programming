#!/usr/bin/python3
""" a module with BaseGeometry calss"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square a rectangle with same width and height"""
    def __init__(self, size):
        """ Initializes the size of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
