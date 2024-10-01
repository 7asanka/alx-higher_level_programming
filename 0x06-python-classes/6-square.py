#!/usr/bin/python3
"""This module defines a square class"""


class Square:
    """
    this is a square class

    Attributes:
        size: the sie of the square
        position: the position of the square

    methods:
        area: return the area of the square
        my_print: prints a square with #
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initializes a square

        Args:
            size: the size of the square
            position: the position of the square
        """
        self.position = position
        self.size = size

    @property
    def size(self):
        """
        __size getter function

        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter function

        Args:
            value: value to set the size
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        """
        returns the proprty
        """
        return self.__property

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculates the area of the square

        Returns:
            the area of the square (size x size)
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints a square with #
        """
        if self.__size == 0:
            print()
            return

        [print() for pos in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()
