#!/usr/bin/python3
"""
This module defines a class representing a square
that inherits from the rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class representing a square that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Creates a new Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x position of the square (default is 0).
            y (int): The y position of the square (default is 0).
            id (int, optional): The identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square's attributes.

        Args:
            *args: A list of positional arguments.
            **kwargs: A dictionary of keyword arguments.
        """
        attributes = ['id', 'size', 'x', 'y']
        for i, arg in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], arg)

        for key, value in kwargs.items():
            if key in attributes:
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square.

        Returns:
            dict: A dictionary containing the square's attributes.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns a string representation of the Square instance.

        Returns:
            str: A string representing the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)
