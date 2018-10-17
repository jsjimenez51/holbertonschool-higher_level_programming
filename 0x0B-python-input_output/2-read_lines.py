#!/usr/bin/python3
"""
Module that defines a read_lines function.
"""


def read_lines(filename="", nb_lines=0):
    """
    Reads n lines of a text file and prints it to stdout
    """
    lineCount = 0
    with open(filename, 'r', encoding='utf-8') as a_file:
        for line in a_file:
            lineCount += 1
            print(line, end="")
            if nb_lines == lineCount:
                break
