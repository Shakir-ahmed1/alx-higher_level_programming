#!/usr/bin/python3
""" a unittest for task base.py """
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ test case for Base class"""

    def test_basic_base(self):
        """ tests the basic test for the base class
            improvements =  checks if the __init__.py exists
        """
        # init with no value
        b1 = Base()
        b2 = Base()
        b3 = Base()
        # init with value then no value
        b4 = Base(12)
        b5 = Base()
        b6 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, 5)

    def test_to_json_string(self):
        dictionary = {"a": 1, "b": 2}
        r2 = {"a": 3, "b": 4}
        json_dictionary = Base.to_json_string([dictionary, r2])
        self.assertEqual(eval(json_dictionary), [dictionary, r2])

        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(eval(json_dictionary), [dictionary])

        json_dictionary = Base.to_json_string([])
        self.assertEqual(eval(json_dictionary), [])

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(eval(json_dictionary), [])

    def test_from_json_string(self):
        dictionary = {"a": 1, "b": 2}
        r2 = '{"a": 3, "b": 4}'
        json_dictionary = Base.from_json_string(str([dictionary, r2]))
        self.assertEqual(json_dictionary, [dictionary, r2])

        json_dictionary = Base.from_json_string(str([dictionary]))
        self.assertEqual(json_dictionary, [dictionary])

        json_dictionary = Base.from_json_string('[]')
        self.assertEqual(json_dictionary, [])

        json_dictionary = Base.from_json_string(None)
        self.assertEqual(json_dictionary, [])

    def test_create(self):
        """ tests the create method """
        r1 = Rectangle(3, 5)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = Rectangle(3, 5, 6)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = Rectangle(3, 5, 7, 8)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = Rectangle(3, 5, 7, 8, 3)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertEqual(r1_d, r2.to_dictionary())

        r1 = {'height': 7, 'width': 1, 'id': 7}
        r2 = Rectangle.create(**r1)
        self.assertEqual(r2.to_dictionary(),
                         {'height': 7, 'width': 1, 'id': 7, 'x': 0, 'y': 0})

        r3 = Rectangle.create(height=3, width=4, id=4, x=1, y=5)
        self.assertEqual(r3.to_dictionary(),
                         {'height': 3, 'width': 4, 'id': 4, 'x': 1, 'y': 5})

        d = {'height': -3, 'width': 4, 'id': 4, 'x': 1, 'y': 5}
        self.assertRaises(ValueError, Rectangle.create, **d)
        d = {'height': 3, 'width': 4, 'id': 4, 'x': [1], 'y': 5}
        self.assertRaises(TypeError, Rectangle.create, **d)
        d = {'height': [3], 'width': 4, 'id': 4, 'x': 1, 'y': 5}
        self.assertRaises(TypeError, Rectangle.create, **d)

 
