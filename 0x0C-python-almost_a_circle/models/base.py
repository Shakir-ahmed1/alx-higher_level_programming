#!/usr/bin/python3
"""
Write the first class Base:
"""
import json
from os.path import exists


class Base:
    """ A Base class for other class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json string representation of list dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves the given list object as json file """
        if not list_objs:
            with open(f"{cls.__name__}.json", 'w') as js:
                js.write('[]')
                return

        new = []
        for ls in list_objs:
            new.append(ls.to_dictionary())
        data = cls.to_json_string(new)
        with open(f"{cls.__name__}.json", 'w') as js:
            js.write(data)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        else:
            return eval(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to instance """
        if cls.__name__ == 'Square':
            a = cls(1)
        else:
            a = cls(1, 1)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        if not exists(f"{cls.__name__}.json"):
            print(f"{cls.__name__}.json")
            return []
        with open(f"{cls.__name__}.json", 'r') as js:
            j = js.read()
            a = cls.from_json_string(j)
            ls = []
            for b in a:
                ls.append(cls.create(**b))
            return ls
