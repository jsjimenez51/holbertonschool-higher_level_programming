#!/usr/bin/python3
"""
Module that defines a class called Student
"""


class Student:
    """
    Defining attributes for the Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiation of the Student object attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of an instance
        """
        value = {}
        if isinstance(attrs, list):
            for key in attrs:
                if key self.__dict__:
                    value[key] = self.__dict__[key]
                return value
            else:
                return self.__dict__
