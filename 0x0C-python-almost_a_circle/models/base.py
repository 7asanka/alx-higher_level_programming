#!/usr/bin/python3
"""
This module defines a class representing the base class
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances from a file"""

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []
