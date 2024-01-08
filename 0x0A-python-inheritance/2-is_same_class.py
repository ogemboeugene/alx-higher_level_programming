#!/usr/bin/python3
"""
Check if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    function checking for object of a
    specified class
    """
    return (type(obj) is a_class)
