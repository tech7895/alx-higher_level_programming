#!/usr/bin/python3

"""The function defines a matrix multiplication function
using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): first matrix.
        m_b (list of lists of ints/floats): second matrix.
    """

    return (np.matmul(m_a, m_b))
