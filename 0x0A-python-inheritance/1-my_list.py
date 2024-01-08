#!/usr/bin/python3
"""
A subclass of list that provides additional functionality.

This class inherits all the behavior of the built-in list class and adds
the ability to print the list in sorted order.
"""


class MyList(list):
    """
    class that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
