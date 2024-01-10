#!/usr/bin/python3
"""
Function that writes an obj to a text file using
JSON rep
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an obj  to a text file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
