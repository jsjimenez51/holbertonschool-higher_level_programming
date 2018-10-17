#!/usr/bin/python3
"""
Module that defines a function called append_write.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file encoded in UTF8 and returns the
    number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as a_file:
        return a_file.write(text)
