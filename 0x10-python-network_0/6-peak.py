#!/usr/bin/python3
""" module that finds peak """


def find_peak(list_of_integers):
    """ finds a pick using the same principles as binary search"""
    if not list_of_integers or len(list_of_integers) == 1:
        return list_of_integers[0] if list_of_integers else None

    mid = len(list_of_integers) // 2
    left = list_of_integers[:mid]
    right = list_of_integers[mid+1:]
    if (not left or list_of_integers[mid] >= left[-1]) and (
            not right or list_of_integers[mid] >= right[0]):
        return list_of_integers[mid]
    elif left and list_of_integers[mid] < left[-1]:
        return find_peak(left)
    else:
        return find_peak(right)
