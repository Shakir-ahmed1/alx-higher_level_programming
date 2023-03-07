#!/usr/bin/python3
def uppercase(str):
    str = str + '\n'
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            print(chr(ord(s)-32), end='')
        else:
            print(s, end='')
