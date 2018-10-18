#!/usr/bin/python3
"""
Module that defines a class called Base
"""


class Base:
    """
    The Base class for all other objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of base instance

        Attributes:
            id (int): id number for base

        Returns:
        None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
