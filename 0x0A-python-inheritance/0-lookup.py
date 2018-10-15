#!/usr/bin/python3
"""
A module that defines a lookup function
"""


def lookup(obj):
    """Returns the list of available attibutes and methods of an objects

    obj: an object that can have attributes and methods defined
    """
    return dir(obj)
