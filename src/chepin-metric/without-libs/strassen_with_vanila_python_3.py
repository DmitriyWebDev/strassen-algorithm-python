from .multiply_two_matrices import multiply_two_matrices
from .split_matrix import split_matrix
from .entrywise_sum_two_matrices import sum_matrices
from .entrywise_subtract_two_matrices import subtract_matrices
from .get_horizontal_stack import get_horizontal_stack
from .get_vertical_stack import get_vertical_stack
from .get_normalized_matrices import get_normalized_matrices

def strassen(matrix_a: list, matrix_b: list) -> list:
    result = []
    matrix_1, matrix_2 = get_normalized_matrices(matrix_a, matrix_b)

    if len(matrix_1) <= 2:
        result = multiply_two_matrices(matrix_1, matrix_2)
        return result

    a, b, c, d = split_matrix(matrix_1)
    e, f, g, h = split_matrix(matrix_2)

    p1 = strassen(sum_matrices(a, d), sum_matrices(e, h))
    p2 = strassen(d, subtract_matrices(g, e))
    p3 = strassen(sum_matrices(a, b), h)
    p4 = strassen(subtract_matrices(b, d), sum_matrices(g, h))
    p5 = strassen(a, subtract_matrices(f, h))
    p6 = strassen(sum_matrices(c, d), e)
    p7 = strassen(subtract_matrices(a, c), sum_matrices(e, f))

    c11 = sum_matrices(sum_matrices(p1, subtract_matrices(p2, p3)), p4)
    c12 = sum_matrices(p5, p3)
    c21 = sum_matrices(p6, p2)
    c22 = sum_matrices(p5, subtract_matrices(subtract_matrices(p1, p6), p7))

    result = get_vertical_stack(get_horizontal_stack(c11, c12), get_horizontal_stack(c21, c22))

    return result
