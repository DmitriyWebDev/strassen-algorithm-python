def split_matrix(matrix):
    n = len(matrix)
    return matrix[:n // 2, :n // 2], matrix[:n // 2, n // 2:], matrix[n // 2:, :n // 2], matrix[n // 2:, n // 2:]
