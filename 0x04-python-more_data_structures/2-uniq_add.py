#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    else:
        sum = 0
        for n in list(set(my_list)):
            sum += n
    return sum
