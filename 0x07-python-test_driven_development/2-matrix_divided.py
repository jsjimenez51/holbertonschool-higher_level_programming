#!/usr/bin/python3
"""
"""


def matrix_divided(matrix, div):
    """
    """
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or \
       all(isinstance(line, list) for line in matrix) is False:
        # check line by line of the matrix for lists
        raise TypeError(matrix_err)
    if len(matrix) == 0 or all(len(line) == 0 for line in matrix):
        # check matrix and each line for inputs > 0
        raise TypeError(matrix_err)
    if all(len(line) == len(matrix[0]) for line in matrix) is False:
        # check if each line is same size
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        # check if div is valid input type
        raise TypeError("div must be a number")
    if div == 0:
        # check if div == 0
        raise ZeroDivisionError("division by zero")
        # divide each element by div rounded 2 places
    return [[round(elem / div, 2) for elem in line] for line in matrix]


if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/2-matrix_divided.txt")
