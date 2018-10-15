#!/usr/bin/python3
"""Module that contains a function that returns whether or not an obj
is an instance of an inherited specifid class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the passed class is an instance of the defined inherited class.
    Args:
        obj: the object being checked.
        a_class: the class used for comparison.
    Returns:
        True if the object is an instance
        False if otherwise
    """
    return (isinstance(obj, a_class))
