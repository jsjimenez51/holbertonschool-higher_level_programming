#!/usr/bin/python3
"""
Module that defines an object that returns the number of lines in a text file.
"""


def number_of_lines(filename=""):
    """
    Function that reads a file then returns the number of lines of text.

    Arg: filename
    """
    lines = 0
    with open(filename, encoding="utf-8") as a_file:
        for line in a_file:
            lines += 1
        return (lines)
