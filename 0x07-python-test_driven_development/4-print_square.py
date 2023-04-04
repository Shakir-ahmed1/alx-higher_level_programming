#!/usr/bin/python3
""" a module that prints a square"""


def print_square(size):
    """prints a square with the spacified size"""
    if (isinstance(size, float) and size < 0) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for s in range(size):
        print("#" * size)
