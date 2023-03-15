#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for m in matrix:
        result.append(list(map(lambda l: l ** 2, m)))
    return result
