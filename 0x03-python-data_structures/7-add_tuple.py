#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    la = len(tuple_a)
    lb = len(tuple_b)
    lsa = [0, 0]
    lsb = [0, 0]
    if la >= 1:
        lsa[0] = tuple_a[0]
    if lb >= 1:
        lsb[0] = tuple_b[0]
    if la >= 2:
        lsa[1] = tuple_a[1]
    if lb >= 2:
        lsb[1] = tuple_b[1]
    return (lsa[0] + lsb[0], lsa[1] + lsb[1])
