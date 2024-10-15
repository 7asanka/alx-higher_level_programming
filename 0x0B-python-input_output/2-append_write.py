#!/usr/bin/python3
"""
Defines the "append_write" function
"""


def append_write(filename="", text=""):
    """appends a string to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
