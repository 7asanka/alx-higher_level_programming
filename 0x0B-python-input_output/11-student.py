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

    def to_json(self, attrs=""):
        """that retrieves a dictionary representation of a Student instance"""
        if attrs == None:
            return self.__dict__
        new_dict = {}
        for ele in attrs:
            try:
                new_dict[ele] = self.__dict__[ele]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
