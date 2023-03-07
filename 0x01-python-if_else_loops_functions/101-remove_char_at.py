#!/usr/bin/python3
def remove_char_at(str, n):
    nstr = ""
    if len(str) <= n or n < 0:
        return str
    for s in range(len(str)):
        if s != n:
            nstr = nstr + str[s]
    return nstr
