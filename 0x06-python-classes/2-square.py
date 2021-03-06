#!/usr/bin/python3
"""
Defines a Square Class
"""


class Square:
    """
    A Class called Square with an attribute:
    size: the size of the Square.
    """
    def __init__(self, size=0):
        """
        Instantiated with size.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
