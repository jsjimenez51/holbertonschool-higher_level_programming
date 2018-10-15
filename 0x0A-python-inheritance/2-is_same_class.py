#!/usr/bin/python3
"""Module that contains a function that returns whether or not an obj
is an instance of a specifid class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the passed class is an instance of the defined class.

    Args:
        obj: the object being checked.
        a_class: the class used for comparison.
    """
    return (type(obj) == a_class)
