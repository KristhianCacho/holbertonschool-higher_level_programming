#!/usr/bin/python3
"""
module: matrix_divided

Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Returns division of all elements of a given matrix

    Arguments:
        matrix(list of list): matrix to work with
        div (int): int to divide the matrix by

    Return:
        new matrix with all elements divided by div
    """

    if type(matrix) is not list:
        raise TypeError ("matrix must be \
                         a matrix (list of list) of integers/floats")

    if len(matrix) is 0:
        raise TypeError ("matrix must be \
                         a matrix (list of list) of integers/floats")

    msize = len(matrix[0])
    if msize is 0:
        raise TypeError ("matrix must be \
                         a matrix (list of list) of integers/floats")

    for row in matrix:
        if len(row) is notmsize:
            raise TypeError ("Each row of the matrix must have the same size")

        if type(row) is not list:
            raise TypeError ("matrix must be \
                             a matrix (list of list) of integers/floats")

        for elem in row:
            if type(elem) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of list) of \
                                integers/floats")

        if type(div) is not int and type (div) is not float:
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")

        for a in matrix:
            for b in a:
                res = round(b / div, 2)

        return (res)
