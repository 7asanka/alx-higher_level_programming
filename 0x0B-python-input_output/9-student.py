#!/usr/bin/python3
"""
Defines a student class
"""


class Student():
    """
    Student class

    attributes:
        first_name: first name
        last_name: last name
        age: age
    """

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation of a Student instance"""
        return self.__dict__
