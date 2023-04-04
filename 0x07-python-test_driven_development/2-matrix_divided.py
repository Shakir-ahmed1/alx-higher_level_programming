#!/usr/bin/python3
""" A module that divides a matrix"""


def matrix_divided(matrix, div):
    """Divides the matrix by the given divider"""
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    ln = -1
    result = []
    for m in matrix:
        if not isinstance(m, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            "of integers/floats")
        if len(m) == ln or ln == -1:
            ln = len(m)
        else:
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) not in [float, int]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        temp = []
        for n in m:
            if type(n) not in [float, int]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")

            a = (n / div).__round__(2)
            temp.append(a)
        result.append(temp)
    return result
