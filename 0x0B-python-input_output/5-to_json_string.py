#!/usr/bin/python3
"""
Defines a function called to_json_string
"""
import json


def to_json_string(my_obj):
    """
    returns a JSON representation of an obj

    Args: myobj: an object
    """
    return json.dumps(my_obj)
