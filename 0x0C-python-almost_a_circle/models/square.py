#!/usr/bin/python3
"""
Module defines a class called Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from the class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation of Square class

        Attributes:
            size (int): size of the square
            x (int): position
            y (int): position
            id (int): instance id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of square (overload of Rectangle attr)
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))
