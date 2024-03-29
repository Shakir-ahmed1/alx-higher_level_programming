#!/usr/bin/python3
"""Square Module"""


class Square:
    """Represents a square with a size"""
    def __init__(self, size=0):
        """Initializes the data and handles error"""
        try:
            if not isinstance(size, int):
                raise TypeError
            if size < 0:
                raise ValueError

            self.__size = size
        except TypeError:
            print("size must be an integer", end="")
            raise
        except ValueError:
            print("size must be >= 0", end="")
            raise
