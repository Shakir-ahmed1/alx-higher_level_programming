#!/usr/bin/python3
""" module that finds peak """

def find_peak(list_of_integers):
    """ finds a pick """
    length = len(list_of_integers)
    li = list_of_integers
    if not list_of_integers:
        return None
    if length == 1:
        return li[0]
    for a in range(length):
        if a == 0 and length > 1 and li[0] >= li[1]:
            return li[0]
        elif a > 1 and a < length - 1:
            if li[a - 1] < li[a] and li[a + 1] <= li[a]:
                return li[a]
        elif a == length - 1 and a > 1 and li[-1] >= li[-2]:
            return li[0]

