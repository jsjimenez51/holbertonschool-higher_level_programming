#!/usr/bin/python3
class MyList(list):
    """
    Class that inherits from list to build a sorted list.
    """
    def print_sorted(self):
        """
        Prints a sorted list.
        """
        print(sorted(self))
