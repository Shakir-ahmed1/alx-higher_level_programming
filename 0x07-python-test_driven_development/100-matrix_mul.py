#!/usr/bin/python3
"""Matrix multiplier using only list"""


def matrix_mul(m_a, m_b):
    """Multiplying matrix using lists"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for a in m_a:
        if not isinstance(a, list):
            raise TypeError("m_a must be a list of lists")
    for b in m_b:
        if not isinstance(b, list):
            raise TypeError("m_b must be a list of lists")
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    for a in m_a:
        for a1 in a:
            if type(a1) not in [float, int]:
                raise TypeError("m_a should contain only integers or floats")
    for b in m_b:
        for b1 in b:
            if type(b1) not in [float, int]:
                raise TypeError("m_b should contain only integers or floats")
    lna = len(m_a[0])
    lnb = len(m_b[0])
    for a in m_a:
        if len(a) != lna:
            raise TypeError("each row of m_a must be of the same size")
    for b in m_b:
        if len(b) != lnb:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    len_a = len(m_a[0])
    len_b = len(m_b)
    result = []
    for a in range(len(m_a)):
        temp = []
        for b in range(len(m_b[0])):
            mul = 0
            for c in range(len(m_b)):
                mul += m_a[a][c] * m_b[c][b]
            temp.append(mul)
        result.append(temp)
    return result
