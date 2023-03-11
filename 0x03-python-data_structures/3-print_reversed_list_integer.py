#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        print('')
    for m in range(1, len(my_list) + 1):
        print("{:d}".format(my_list[m * -1]))
