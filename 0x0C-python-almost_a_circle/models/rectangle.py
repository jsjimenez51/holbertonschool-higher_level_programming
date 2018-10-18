#!/usr/bin/python3
"""
Module defines a class called Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from the class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation of Rectangle class

        Attributes:
            width (int): width of the rectangle
            height (int): hegiht of rectangle
            x (int):
            y (int):
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """
            Returns the width of the Rectangle
            """
            return (self.__width)

        @width.setter
        def width(self, value):
            """
            Sets the value of width

            Attributes:
                value (int): value of the width
            """
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value <= 0:
                raise ValueError('width must be > 0')
            self.__width = value

        @property
        def height(self):
            """
            Returns the height of the Rectangle
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            Set the value of height

            Attributes:
                value (int): value of the height
            """
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if value <= 0:
                raise ValueError('height must be > 0')
            self.__height = value
