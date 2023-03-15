#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ls = []
    for d in a_dictionary:
        if a_dictionary[d] == value:
            ls.append(d)
    for j in ls:
        del a_dictionary[j]
    return a_dictionary
