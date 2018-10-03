#!/usr/bin/python3
"""
Defines a Square Class
"""


class Square:
    """
    A Class called Square with an attribute:
    size: the size of the Square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiated with size.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """
        A public method that returns the area of the Square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to stdout using the # or empty line if 0.
        """
        if self.__size == 0:
            print()
        else:
            x, y = self.__position
            for i in range(y):
                print()
            for i in range(self.__size):
                print(' ' * x, end='')
                print('#' * self.__size)

    @property
    def position(self):
        """
        Private attribute that returns the position of the Square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the value for the __position attribute.
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if type(x) is not int or type(y) is not int or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
