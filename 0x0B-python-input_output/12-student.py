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
        if not attrs:
            return (self.__dict__)

        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})
