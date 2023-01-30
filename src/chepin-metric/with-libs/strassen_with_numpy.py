import numpy as np

# source code - https://gist.github.com/syphh/1cb6b9bb57a400873fa9d05cd1ee7cc3

def brute_force(A, B):
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    C = np.array([[0] * p for i in range(n)])
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C


def split(matrix):
    n = len(matrix)
    return matrix[:n // 2, :n // 2], matrix[:n // 2, n // 2:], matrix[n // 2:, :n // 2], matrix[n // 2:, n // 2:]


def strassen_with_numpy(A, B):
    if len(A) <= 2:
        return brute_force(A, B)
    a, b, c, d = split(A)
    e, f, g, h = split(B)
    p1 = strassen_with_numpy(a + d, e + h)
    p2 = strassen_with_numpy(d, g - e)
    p3 = strassen_with_numpy(a + b, h)
    p4 = strassen_with_numpy(b - d, g + h)
    p5 = strassen_with_numpy(a, f - h)
    p6 = strassen_with_numpy(c + d, e)
    p7 = strassen_with_numpy(a - c, e + f)
    C11 = p1 + p2 - p3 + p4
    C12 = p5 + p3
    C21 = p6 + p2
    C22 = p5 + p1 - p6 - p7
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C
