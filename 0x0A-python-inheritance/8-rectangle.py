#!/usr/bin/python3
"""
defines Rectangle class
"""


bg = __import__('7-base_geometry')


class Rectangle(bg.BaseGeometry):
    """a Rectangle class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
