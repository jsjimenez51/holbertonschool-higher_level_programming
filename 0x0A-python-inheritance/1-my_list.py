#!/usr/bin/python3
"""
Module that defines a class called MyList.
"""


class MyList(list):
    """Class that inherits from list to build a sorted list.
    """

    def print_sorted(self):
        """Prints a sorted list.
        """
        print(sorted(self))

if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/1-my_list.txt")
