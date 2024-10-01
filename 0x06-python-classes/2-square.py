#!/usr/bin/python3
"""This module defines a square class"""


class Square:
    """
    this is a square class

    Attributes:
        __size: the sie of the square

    methods:
        __init__: initializes the class
    """

    def __init__(self, size=0):
        """
        initializes a square

        Args:
            size: the size of the square
        """
        self.__size = size

        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
