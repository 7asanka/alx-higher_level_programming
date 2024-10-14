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

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """__str__ function"""
        return "[{:s}] {:d}/{:d}".format(type(self).__name__, self.__width,
                                         self.__height)
