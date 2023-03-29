#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """Defines a single node"""

    def __init__(self, data, next_node=None):
        """Initailze the data"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not next_node or isinstance(next_node, type(self)):
            pass
        else:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Data Setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Node setter"""
        if not value or isinstance(value, type(self)):
            pass
        else:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Creates singly linked list"""

    def __init__(self):
        """Initialize the data"""
        self.__head = None

    def sorted_insert(self, value):
        """Add value according it's value"""
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            temp = self.__head
            while temp.next_node and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """String representation of The class"""
        temp = self.__head
        ls = []
        if not temp:
            return ""
        while temp:
            ls.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(ls)
