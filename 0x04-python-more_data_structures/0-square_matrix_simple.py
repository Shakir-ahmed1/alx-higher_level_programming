#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for m in matrix:
        result.append(list(map(lambda d: d ** 2, m)))
    return result
