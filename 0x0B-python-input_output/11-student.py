#!/usr/bin/python3
""" module for Student class"""


class Student:
    """ Student with name and age """
    def __init__(self, first_name, last_name, age):
        """ Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns a dicitonary based on the attrs """
        dc = vars(self)
        if attrs is None:
            return dc
        newdc = dict()
        for a in attrs:
            if a in dc:
                newdc[a] = dc[a]
        return newdc

    def reload_from_json(self, json):
        """ replaces all attributes of the class using the json variable"""
        for d in json:
            if hasattr(self,d):
                setattr(self, d, json[d])
