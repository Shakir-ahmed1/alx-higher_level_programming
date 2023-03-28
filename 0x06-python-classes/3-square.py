#!/usr/bin/python3
"""Square Modlue"""


class Square:
    """Square with a size"""
    def __init__(self, size=0):
        """Initializes the size and handles error"""
        try:
            if isinstance(size, str):
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
    def area(self):
        """Calculates the area of the square"""
        return (self.__size * self.__size)
