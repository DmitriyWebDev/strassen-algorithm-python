import numpy as np


def multiply_two_matrices(A, B):
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    C = np.array([[0] * p for i in range(n)])
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C
