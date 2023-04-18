#!/usr/bin/python3
"""
Write the first class Base:
"""
import json
import csv
import turtle
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
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates a new instance with the given dictionary """
        if cls.__name__ == 'Square':
            a = cls(1)
        else:
            a = cls(1, 1)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        if not exists(f"{cls.__name__}.json"):
            return []
        with open(f"{cls.__name__}.json", 'r') as js:
            j = js.read()
            a = cls.from_json_string(j)
            ls = []
            for b in a:
                ls.append(cls.create(**b))
            return ls

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves the list object in csv file """
        with open(f"{cls.__name__}.csv", "w") as f:
            a = csv.writer(f)
            if cls.__name__ == 'Rectangle':
                for ls in list_objs:
                    temp = []
                    ls = ls.to_dictionary()
                    temp.append(ls["id"])
                    temp.append(ls["width"])
                    temp.append(ls["height"])
                    temp.append(ls["x"])
                    temp.append(ls["y"])
                    a.writerow(temp)
            if cls.__name__ == 'Square':
                for ls in list_objs:
                    temp = []
                    ls = ls.to_dictionary()
                    temp.append(ls["id"])
                    temp.append(ls["size"])
                    temp.append(ls["x"])
                    temp.append(ls["y"])
                    a.writerow(temp)

    @classmethod
    def load_from_file_csv(cls):
        """ loads list of objects from csv file """
        with open(f"{cls.__name__}.csv") as f:
            a = csv.reader(f)
            result = []
            if cls.__name__ == "Rectangle":
                for b in a:
                    c = dict()
                    c["id"] = int(b[0])
                    c["width"] = int(b[1])
                    c["height"] = int(b[2])
                    c["x"] = int(b[3])
                    c["y"] = int(b[4])
                    result.append(cls.create(**c))
            if cls.__name__ == "Square":
                for b in a:
                    c = dict()
                    c["id"] = int(b[0])
                    c["size"] = int(b[1])
                    c["x"] = int(b[2])
                    c["y"] = int(b[3])
                    result.append(cls.create(**c))

            return result

    def draw(list_rectangles, list_squares):
        for lr in list_rectangles:
            turtle.penup()
            turtle.goto(lr.x, lr.y)
            turtle.pendown()

            for i in range(2):
                turtle.forward(lr.width)
                turtle.right(90)
                turtle.forward(lr.height)
                turtle.right(90)

        for lr in list_squares:
            turtle.penup()
            turtle.goto(lr.x, lr.y)
            turtle.pendown()

            for i in range(2):
                turtle.forward(lr.size)
                turtle.right(90)
                turtle.forward(lr.size)
                turtle.right(90)
