#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    student = ''
    maximum = -1
    for a, b in a_dictionary.items():
        if b > maximum:
            maximum = b
            student = a
    return student
