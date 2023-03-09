#!/usr/bin/python3
import hidden_4
for d in dir(hidden_4):
    if d[:2] != "__":
        print(d)
