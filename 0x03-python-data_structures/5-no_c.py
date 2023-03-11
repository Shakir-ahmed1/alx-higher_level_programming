#!/usr/bin/python3
def no_c(my_string):
    str = ''
    for s in my_string:
        if s.upper() == "C":
            continue
        else:
            str = str + s
    return str
