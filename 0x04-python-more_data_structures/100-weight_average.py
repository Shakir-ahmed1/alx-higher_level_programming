#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = 0
    weight = 0
    for a in my_list:
        score += a[0] * a[1]
        weight += a[1]
    return score / weight
