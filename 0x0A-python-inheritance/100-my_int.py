#!/usr/bin/python3
"""Write a class MyInt that inherits from in
MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module
"""


class MyInt(int):
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
