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
        number_of_instances: self explanatory

    methods:
        height: height getter and setter
        width: width getter and setter
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """returns the rectanglse area"""
        return self.height * self.width

    def perimeter(self):
        """returns the rectangles perimeter"""
        if self.height <= 0 or self.width <= 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rect_1_bigger = rect_1.area() >= rect_2.area()
        if rect_1_bigger:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a square with the size"""
        return cls(size, size)

    def __str__(self):
        """__str__ for rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        string = "\n".join("{}".format(str(self.print_symbol)) * self.__width
                           for i in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation
        that can recreate the rectangle instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """runs when deleting a
        rectangle instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
