#!/usr/bin/python3
"""
Module that returns the sum of two integers: a, b.
TypeError is raise if input is not a valid integer or float.
Return will be an integer type value.
"""


def add_integer(a, b=98):
    """ add_integer: Checks if input type is correct, then returns sum of values
    args: passed a and b
    return: int type sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a + b)


if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
