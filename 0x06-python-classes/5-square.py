#!/usr/bin/python3
"""This module defines a square class"""


class Square:
    """
    this is a square class

    Attributes:
        size: the sie of the square

    methods:
        area: return the area of the square
        my_print: prints a square with #
    """

    def __init__(self, size=0):
        """
        initializes a square

        Args:
            size: the size of the square
        """
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
        for i in range(self.__size):
            for j in range(self.__size):
                if j == (self.__size - 1):
                    print("#", end="\n")
                else:
                    print("#", end="")
