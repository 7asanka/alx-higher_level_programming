#!/usr/bin/python3
"""
This is the "0-add_integer" module
"""

def add_integer(a, b=98):
    """
    adds 2 numbers

    args:
        a: first number
        b: second number

    Returns:
        the sum of two numbers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
