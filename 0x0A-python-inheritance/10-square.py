#!/usr/bin/python3
"""
module defines a Square class
"""


rec = __import__('9-rectangle')


class Square(rec.Rectangle):
    """class resembles a square"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the size of the square"""
        return self.__size**2
