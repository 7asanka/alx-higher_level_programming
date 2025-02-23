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
        """init function

            args:
                first_name: students first name
                last_name: students last name
                age: students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=""):
        """that retrieves a dictionary representation of a Student instance

            args:
                attrs (optional): list of attributes

            returns:
                that retrieves a dictionary representation
                of a Student instance
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
