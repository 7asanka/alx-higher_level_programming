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

    def test_base_create(self):
        dictionary = {"id": 89, "width": 10, "height": 4, "x": 2, "y": 1}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 89)

    def test_base_create(self):
        dictionary = {"id": 89, "width": 10, "height": 4, "x": 2, "y": 1}
        r= Rectangle.create(**dictionary)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 89)

    def test_update(self):
        r = Rectangle(10, 2)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_empty_args(self):
        r = Rectangle(5, 5)
        r.update()
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_rectangle_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

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
