#!/usr/bin/python3
"""unittests module for Rectangle.py"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unittest for Rectangle class"""

    def setUp(self):
        Rectangle._Base__nb_objects = 0

    def test_initialization(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_height_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_area(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

    def test_update(self):
        r = Rectangle(10, 2)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 1, 1)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, {
            'id': 1,
            'width': 10,
            'height': 2,
            'x': 1,
            'y': 1
        })


if __name__ == "__main__":
    unittest.main()
