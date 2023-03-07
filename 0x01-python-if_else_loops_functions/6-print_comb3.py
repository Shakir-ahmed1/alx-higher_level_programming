#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if b > a and a != 8:
            print("{}{}".format(a, b), end=", ")
print(89)
