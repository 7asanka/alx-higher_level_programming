#!/usr/bin/python3
"""
this module defines a class
representing a rectangle
"""


class Rectangle:
    """
    class that represents a rectangle

    attributes:
        height: the height of the rectangle
        width: the width of the rectangle

    methods:
        height: height getter and setter
        width: width getter and setter
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise ("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
