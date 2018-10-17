#!/usr/bin/python3
"""
A module that defines a function called from_json_string
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.
    """
    return json.loads(my_str)
