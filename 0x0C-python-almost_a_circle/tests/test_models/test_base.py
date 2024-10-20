#!/usr/bin/python3
"""unittest module for base.py"""


import unittest
from models.base import Base


class TestBaseInit(unittest.TestCase):
    """unittest for __init__"""

    def test_no_args(self):
        """test base instantiation with no args"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_assignment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(42)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 42)
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])

    def test_load_from_file_no_file(self):
        self.assertEqual(Base.load_from_file(), [])

if __name__ == "__main__":
    unittest.main()
