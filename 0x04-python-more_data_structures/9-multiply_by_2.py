#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for a, b in a_dictionary.items():
        new_dict[a] = b * 2
    return new_dict
