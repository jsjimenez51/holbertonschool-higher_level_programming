#!/usr/bin/python3
"""
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print('{:s}'.format('#' * size))


if __name__ == '__main__':
        import doctest
        doctest.testfile("./tests/4-print_square.txt")
