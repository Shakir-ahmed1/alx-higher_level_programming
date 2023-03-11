#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for a in range(len(matrix)):
        c = len(matrix[a])
        for b in range(c):
            if b == c - 1:
                print("{:d}".format(matrix[a][b]))
            else:
                print("{:d} ".format(matrix[a][b]), end=" ")
