#!/usr/bin/python3
"""
Defines the "load_from_json_file" func
"""


import json


def load_from_json_file(filename):
    """crate and object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
