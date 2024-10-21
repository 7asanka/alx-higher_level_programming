#!/usr/bin/python3
"""unittest module for square.py"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """unittest for the Square class"""

    def setUp(self):
        Square._Base__nb_objects = 0

    def test_initialization(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_size_validation(self):
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_update(self):
        s = Square(5)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_empty_args(self):
        s = Square(5)
        s.update()
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_inheritance(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        s.size = 7
        self.assertEqual(s.width, 7)
        self.assertEqual(s.height, 7)

    def test_size_boundary(self):
        s = Square(1)
        self.assertEqual(s.size, 1)
        with self.assertRaises(ValueError):
            Square(0)

    def test_to_dictionary(self):
        s = Square(5, 1, 1, 1)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, {
            'id': 1,
            'size': 5,
            'x': 1,
            'y': 1
        })


if __name__ == "__main__":
    unittest.main()

