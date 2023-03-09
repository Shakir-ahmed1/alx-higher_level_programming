#!/usr/bin/python3
from sys import argv as args

if __name__ == '__main__':
    if len(args) == 1:
        print("0 arguments.")
    elif len(args) == 2:
        print("1 argument:")
        print("1: {}".format(args[1]))
    else:
        print("{} arguments:".format(len(args) - 1))
        for a in range(1, len(args)):
            print("{}: {}".format(a, args[a]))
