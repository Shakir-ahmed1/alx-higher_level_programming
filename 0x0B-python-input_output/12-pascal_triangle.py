#!/usr/bin/python3
""" pascal triangle module"""


def pascal_triangle(n):
    result = []
    temp = []
    holder = []
    if n <= 0:
        return []
    for a in range(n):
        if a == 0:
            holder = [1]
            result.append(holder)
            continue
        for b in range(a + 1):
            if b == 0 or b == a:
                temp.append(1)
                continue
            temp.append(holder[b-1] + holder[b])
        result.append(temp)
        holder = temp
        temp = []
    return result
