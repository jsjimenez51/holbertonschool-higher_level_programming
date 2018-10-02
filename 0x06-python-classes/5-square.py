#!/usr/bin/python3
"""
Defines a Square Class
"""


class Square:
    """
    A Class called Square with an attribute:
    size: the size of the Square.
    """
    def __init__(self, size=0):
        """
        Instantiated with size.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        A public method that returns the area of the Square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to stdout using the # or empty line if 0.
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)

    @property
    def size(self):
        """
        Private __size attribute that returns the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value for the __size attribute.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
