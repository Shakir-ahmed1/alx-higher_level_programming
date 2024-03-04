#!/usr/bin/python3
""" A module for lazy matrix multipliers"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Matrix multiplication of lists"""
    return numpy.matmul(m_a, m_b)
