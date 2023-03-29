#!/usr/bin/python3
"""Square Modlue"""


class Square:
    """Square with a size"""
    def __init__(self, size=0):
        """Initializes the size and handles error"""
        try:
            if not (isinstance(size, int) or isinstance(size, float)):
                raise TypeError
            if size < 0:
                raise ValueError

            self.__size = size
        except TypeError:
            print("size must be a number", end="")
            raise
        except ValueError:
            print("size must be >= 0", end="")
            raise

    def area(self):
        """Calculates the area of the square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """get size"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """size setter"""
        try:
            if not (isinstance(size, int) or isinstance(size, float)):
                raise TypeError
            if size < 0:
                raise ValueError

            self.__size = size
        except TypeError:
            print("size must be a number", end="")
            raise
        except ValueError:
            print("size must be >= 0", end="")
            raise

    def __lt__(self, other):
        """Comparision operator"""
        return self.size < other.size

    def __le__(self, other):
        """Comparision operator"""
        return self.size <= other.size

    def __eq__(self, other):
        """Comparision operator"""
        return self.size == other.size

    def __ne__(self, other):
        """Comparision operator"""
        return self.size != other.size

    def __gt__(self, other):
        """Comparision operator"""
        return self.size > other.size

    def __ge__(self, other):
        """Comparision operator"""
        return self.size >= other.size
