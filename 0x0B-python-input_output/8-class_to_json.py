#!/usr/bin/python3
"""
Function that returns the dictionary description with
simple data structure for json
serialization of obj
"""


def class_to_json(obj):
    """
    function that returns dict descp
    """
    return (obj.__dict__)
