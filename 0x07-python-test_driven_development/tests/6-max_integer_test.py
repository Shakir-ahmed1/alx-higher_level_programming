#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the given funcitons"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, [1, 3, '4', 2])
        self.assertRaises(TypeError, max_integer, {1, 3, 4, 2})
        self.assertEqual(max_integer((1, 2, 4, 3)), 4)
        self.assertEqual(max_integer([1, -2, -4, 3, 0]), 3)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer({1: 1, 3: 2, 4: 3, 2: 4, 0: 9}), 9)
        self.assertRaises(KeyError, max_integer, {1: 1, 3: 2, 4: 3, 2: 4})
