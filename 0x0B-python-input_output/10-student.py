#!/usr/bin/python3
""" module for Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dc = vars(self)
        if attrs == None:
            return dc
        newdc = dict()
        for a in attrs:
            if a in dc:
                newdc[a] = dc[a]
        return newdc
