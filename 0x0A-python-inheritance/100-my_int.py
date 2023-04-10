#!/usr/bin/python3
"""Write a class MyInt that inherits from in
MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module
"""


class MyInt(int):
    """ My new integer """
    def __eq__(self, other):
        """ it changes == operator to inequailty operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ it changes =! operator to equailty operator """
        return super().__eq__(other)
