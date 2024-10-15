#!/usr/bin/python3
"""
Defines th "write_file" function
"""


def write_file(filename="", text=""):
    """writes a string into a file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
