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
        if attrs is not None and isinstance(attrs, list):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
