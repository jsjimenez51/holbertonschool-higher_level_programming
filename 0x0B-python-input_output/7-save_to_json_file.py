#!/usr/bin/python3
"""
Module that defines save_to_json_file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation

    Args:
    my_obj: the object that is written to the file
    filename: the file to write the object to

    """
    with open(filename, 'w') as a_file:
        a_file.write(json.dumps(my_obj))
