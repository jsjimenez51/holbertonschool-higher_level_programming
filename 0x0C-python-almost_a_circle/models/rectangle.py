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

    @property
    def x(self):
        """
        Returns x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the value of x

        Attribute:
        value (int): value to set x to
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        Returns y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value of y

        Attributes:
        value (int): valut to set y to
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return (self.width * self.height)

    def display(self):
        """
        Prints the Rectangle with #s to stdout
        """
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(' ' * self.x + '#' * self.__width)

    def __str__(self):
        """
        Overrides the Rectanlge class __str__ method
        """
        return ('[Rectangle] ({}) {}/{} - {}/{}'
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        """
        update = len(args)
        if update is not 0:
            if update >= 1:
                self.id = args[0]
            if update >= 2:
                self.width == args[1]
            if update >= 3:
                self.height == args[2]
            if update >= 4:
                self.__x = args[3]
            if update >= 5:
                self.__y = args[4]
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)
