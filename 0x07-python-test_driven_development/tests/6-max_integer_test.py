#!/usr/bin/python3
"""
unittest for "max_integer"
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_int(self):
        """test normal use"""
        self.assertEqual(max_integer([5, 2, 3, 5.5]), 5.5)
        self.assertEqual(max_integer([1]), 1)

    def test_no_args(self):
        """test no args passed"""
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        """test empty list passed"""
        self.assertIsNone(max_integer([]))
