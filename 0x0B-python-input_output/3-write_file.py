#!/usr/bin/python3
"""
Module that defines a write_file Function.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of chars wrote
    """
    with open(filename, 'w', encoding='utf-8') as a_file:
        return (a_file.write(text))
