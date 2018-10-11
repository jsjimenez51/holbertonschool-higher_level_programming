#!/usr/bin/python3
"""
Defines a Rectangle class Module.
"""


class Rectangle:
    """
    Defines a Rectangle object class.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiates the Rectangle.
        Args:
        width (int)
        height (int)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Returns the area of the Rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """
        Prints the Rectangle in #'s.
        """
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            return '\n'.join((str(self.print_symbol) * self.width)
                             for row in range(self.height))

    def __repr__(self):
        """
        Returns a representation string to the object
        """
        return ('Rectangle({:d}, {:d})'.format(self.width, self.height))

    def __del__(self):
        """
        Deletes an instance of the object and prints a message for verification
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectanlges and returns the largest based on size
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
