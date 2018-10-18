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

    @property
    def size(self):
        """
        Returns the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of square (overload of Rectangle attr)
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    def update(self, *args, **kwargs):
        """
        Assigns new arguments to each attribute
        """
        update = len(args)
        if update is not 0:
            if update >= 1:
                self.id = args[0]
            if update >= 2:
                self.size = args[1]
            if update >= 3:
                self.x = args[2]
            if update >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
