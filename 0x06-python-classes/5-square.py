#!/usr/bin/python3
"""Square Modlue"""


class Square:
    """Square with a size"""
    def __init__(self, size=0):
        """Initializes the size and handles error"""
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

    def my_print(self):
        """Prints the size of square using #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#"*self.__size)
