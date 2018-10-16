#!/usr/bin/python3
"""
Module that defines a class called Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class called square that inherits from the Rectangle Module.
    """

    def __init__(self, size):
        """
        Instantiates a Square.
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)
