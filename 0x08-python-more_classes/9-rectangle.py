#!/usr/bin/python3
"""
This module defines a class representing a rectangle.
"""


class Rectangle:
    """
    Class that represents a rectangle.

    Attributes:
        number_of_instances (int): Keeps track of the number of instances.
        print_symbol (any): Symbol used for string
        representation (default is '#').

    Methods:
        height (getter/setter): Gets or sets the height.
        width (getter/setter): Gets or sets the width.
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        bigger_or_equal(): Returns the rectangle with
        the greater or equal area.
        square(): Creates a square with the specified size.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle's perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the rectangle with the greater or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the larger or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a square (rectangle with equal width and height).

        Args:
            size (int): The size of the square's sides.

        Returns:
            Rectangle: A new rectangle instance with
            width and height equal to size.
        """
        return cls(size, size)

    def __str__(self):
        """
        Returns a string representation of the
        rectangle using the print_symbol.

        Returns:
            str: The string representation of the rectangle.
                 If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.__width
                         for _ in range(self.__height))

    def __repr__(self):
        """
        Returns a string representation that
        can recreate the rectangle instance.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message and decrements the instance
        count when a rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
