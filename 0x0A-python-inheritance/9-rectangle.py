#!/usr/bin/python3
"""
Module that defines a Rectangle
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

    def area(self):
        """
        defines the area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
