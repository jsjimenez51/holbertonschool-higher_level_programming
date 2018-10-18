#!/usr/bin/python3
"""
Module that defines a class called Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of list_dictionaries

        Args:
            list_dictionaries ([]): a list of dictionaries
        """
        if not list_dictionaries or list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
