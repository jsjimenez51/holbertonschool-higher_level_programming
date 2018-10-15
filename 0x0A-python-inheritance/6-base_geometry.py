#!/usr/bin/python3
"""
Module that contains a class BaseGeometry
"""


class BaseGeometry:
    """
    contains a public instance and raises an exception when necessary
    """
    def area(self):
        """
        public instance for area
        """
        raise Exception('area() is not implemented')
