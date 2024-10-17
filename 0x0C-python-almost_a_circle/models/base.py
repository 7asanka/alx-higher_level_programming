#!/usr/bin/python3
"""
This module defines a class representing the base class
"""


class Base:
    """
    class representing the base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes a new base

        args:
            id: new base id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
