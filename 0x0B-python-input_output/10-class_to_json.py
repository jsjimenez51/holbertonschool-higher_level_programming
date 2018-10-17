#!/usr/bin/python3
"""
Module defines a function called class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object
    """
    return obj.__dict__
