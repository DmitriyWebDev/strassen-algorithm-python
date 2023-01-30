import numpy as np
from .split_matrix import split_matrix
from .multiply_two_matrices import multiply_two_matrices


def strassen(matrix_a, matrix_b):
    result = []

    if len(matrix_a) <= 2:
        result = multiply_two_matrices(matrix_a, matrix_b)
        return result

    a, b, c, d = split_matrix(matrix_a)
    e, f, g, h = split_matrix(matrix_b)

    p1 = strassen(a + d, e + h)
    p2 = strassen(d, g - e)
    p3 = strassen(a + b, h)
    p4 = strassen(b - d, g + h)
    p5 = strassen(a, f - h)
    p6 = strassen(c + d, e)
    p7 = strassen(a - c, e + f)

    c11 = p1 + p2 - p3 + p4
    c12 = p5 + p3
    c21 = p6 + p2
    c22 = p5 + p1 - p6 - p7

    result = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return result
