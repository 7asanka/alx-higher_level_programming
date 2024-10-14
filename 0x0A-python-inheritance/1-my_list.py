#!/usr/bin/python3
"""
defines the calass My_List
"""


class MyList(list):
    """
    class that inherits list
    """
    def __init__(self):
        """ initialize MyList"""
        super().__init__()

    def print_sorted(self):
        """prings the list sorted"""
        print([i for i in sorted(self)])
