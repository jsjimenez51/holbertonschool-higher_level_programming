#!/usr/bin/python3
"""
Defines a Rectangle class Module.
"""


class Rectangle:
    """
    Defines a Rectangle object class.
    """

    def __init__(self, width=0, height=0):
        """
        Instantiates the Rectangle.

        Args:
        width (int)
        height (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle.

        Args:
        value (int): width value to set.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle.

        Args:
        value (int)
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
