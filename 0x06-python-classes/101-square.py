#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square with a size"""

    def __init__(self, size=0, position=(0, 0)):
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

        try:
            if (not isinstance(position, tuple)
                    or len(position) != 2
                    or not isinstance(position[0], int)
                    or not isinstance(position[1], int)
                    or position[0] < 0 or position[1] < 0):
                raise TypeError

            self.__position = position
        except TypeError:
            print("position must be a tuple of 2 positive integers", end="")
            raise

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """get size"""
        return self.__size

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

    @property
    def position(self):
        """Position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter"""
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple"
                            " of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Prints the size of square using #"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """Prints the size of square using #"""
        ls = []
        if self.__size == 0:
            return ""
        for j in range(self.__position[1]):
            ls.append("\n")
        for i in range(self.__size):
            ls.append(" " * self.__position[0])
            if i == self.__size - 1:
                ls.append("#" * self.__size)
            else:
                ls.append("#" * self.__size + "\n")
        return "".join(ls)
