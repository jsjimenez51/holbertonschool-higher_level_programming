#!/usr/bin/python3
"""
Module that defines load_from_json_file
"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    """
    with open(filename, 'r', encoding ='utf-8') as a_file:
        return json.load(a_file)
