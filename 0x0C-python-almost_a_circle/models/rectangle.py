#!/usr/bin/python3
""" a module that defines Rectange """
from models.base import Base


class Rectangle(Base):
    """ A clase with Rectangle representation """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ intializes the attributes and assigns an id"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ the area of the rectangle width x height """
        return self.__height * self.__width

    def display(self):
        """ displays the rectangle using # according to height and width"""
        for b in range(self.__y):
            print("\n", end="")
        for a in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """ assigns the values to the attributes using args """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
            return
        if kwargs:
            if kwargs.get("id") is not None:
                self.id = kwargs["id"]
            if kwargs.get("height") is not None:
                self.height = kwargs["height"]
            if kwargs.get("width") is not None:
                self.width = kwargs["width"]
            if kwargs.get("x") is not None:
                self.x = kwargs["x"]
            if kwargs.get("y") is not None:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ converts the rectangle to dicitonary """
        dc = {}
        dc["id"] = self.id
        dc["width"] = self.width
        dc["height"] = self.height
        dc["x"] = self.x
        dc["y"] = self.y
        return dc

    def __str__(self):
        """ string representation of the rectangle class """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width, self.__height)
