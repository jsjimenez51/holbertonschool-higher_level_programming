#!/usr/bin/python3
"""
Module with a function that verifies if an object is an instance of a class
that inherits from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Function returns True or False based on object.
    """
    if type(obj) is not a_class:
        return(issubclass(type(obj), a_class))
