#!/usr/bin/python3
"""a simple inheritance"""


class MyList(list):
    """Enables sorted printing for the list object"""
    def __init__(self):
        """Initializes the class"""
        super().__init__()

    def print_sorted(self):
        """Sortes the given length by size"""
        print(sorted(self))
