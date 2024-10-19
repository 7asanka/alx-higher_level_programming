#!/usr/bin/python3
"""
This module definse a class representing a rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    a class representing a rectangle

    inherits Base class

    attributes:
        width: the width of the rectangle
        height: the height of the rectangle
        x:
        y:

    methods:
        area: returns the area of the rectangle
        display: prints the rectangle using the '#' char
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle

        args:
            width: width of the rectangle
            height: heigt of the rectangle
            x:
            y:
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays the rectangle using the char '#'"""

        [print() for pos_y in range(self.__y)]

        for i in range(self.__height):
            print(" " * self.__x, "#" * self.__width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        i = 0
        for arg in args:
            if i == 0:
                self.id = arg
            elif i == 1:
                self.width = arg
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg
            i += 1

        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            elif k == "width":
                self.width = v
            elif k == "height":
                self.height = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }

    def __str__(self):
        """string representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
