#!/usr/bin/python3
"""
Function that returns the JSON representation
of an object
"""
import json


def to_json_string(my_obj):
    """
    function to return JSON
    representation
    """
    return (json.dumps(my_obj))
