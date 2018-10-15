#!/usr/bin/python3
"""
Module that defines the following classes" BaseGeometry & Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
