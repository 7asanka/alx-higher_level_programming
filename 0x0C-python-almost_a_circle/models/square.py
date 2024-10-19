#!/usr/bin/python3
"""
This module defines a class representing a square
that inherits from the rectangle calss
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class representing a square that inherits for rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        crates new Square instance

        args:
            size: size of the square
            x: x position of the square
            y: y position of the square
            id: id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size settet"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the squares value"""

        i = 0
        for arg in args:
            if i == 0:
                self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg
            i += 1

        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            elif k == "size":
                self.size = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v

    def to_dictionary(self):
        """dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """string representation of the square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)
