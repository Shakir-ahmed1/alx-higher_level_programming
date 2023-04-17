#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square: a rectangle with the same height and width """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor for Square class """
        super().__init__(size, size, x, y, None)
    
    @property
    def size(self):
        """ returns the size of square """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size of the square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns the values to the attributes using args """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
            return
        if kwargs:
            if kwargs.get("id") is not None:
                self.id = kwargs["id"]
            if kwargs.get("size") is not None:
                self.width = kwargs["size"]
            if kwargs.get("x") is not None:
                self.x = kwargs["x"]
            if kwargs.get("y") is not None:
                self.y = kwargs["y"]
 
    def to_dictionary(self):
        """ converts the rectangle to dicitonary """
        dc = {}
        dc["id"] = self.id
        dc["size"] = self.size
        dc["x"] = self.x
        dc["y"] = self.y
        return dc

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width)

