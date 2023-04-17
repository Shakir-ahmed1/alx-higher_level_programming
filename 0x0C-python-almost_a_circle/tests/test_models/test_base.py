#!/usr/bin/python3
""" a unittest for task base.py """
from models.base import Base
import unittest


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
        json_dictionary = Base.to_json_string([dictionary,r2])
        self.assertEqual(eval(json_dictionary), [dictionary,r2])

        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(eval(json_dictionary), [dictionary])

        json_dictionary = Base.to_json_string([])
        self.assertEqual(eval(json_dictionary), [])

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(eval(json_dictionary), [])

    def test_from_json_string(self):
        dictionary = {"a": 1, "b": 2}
        r2 = '{"a": 3, "b": 4}'
        json_dictionary = Base.from_json_string(str([dictionary,r2]))
        self.assertEqual(json_dictionary, [dictionary,r2])

        json_dictionary = Base.from_json_string(str([dictionary]))
        self.assertEqual(json_dictionary, [dictionary])

        json_dictionary = Base.from_json_string('[]')
        self.assertEqual(json_dictionary, [])

        json_dictionary = Base.from_json_string(None)
        self.assertEqual(json_dictionary, [])
