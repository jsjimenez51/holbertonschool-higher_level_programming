#!/usr/bin/python3
"""
Module that defines a class that opens and reads a file.
"""


def read_file(filename=""):
    """
    Object that opens and reads a file
    """
    with open(filename, encoding="utf-8") as a_file:
        for line in a_file:
            print(line, end="")
