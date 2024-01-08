#!/usr/bin/python3
"""
Contains a function that returns
the list of available attributes and methods
of an object
"""


def lookup(obj):
    """
    function that returns the list of available
    attributes, methods and objects
    """
    return (dir(obj))
