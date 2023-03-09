#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    for d in dir(hidden_4):
        if d[:2] != "__":
            print(d)
