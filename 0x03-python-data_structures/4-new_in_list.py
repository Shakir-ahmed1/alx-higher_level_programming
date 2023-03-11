#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l2 = my_list[:]
    if idx < 0 or len(my_list) <= idx:
        return l2
    else:
        l2[idx] = element
        return l2
