from .multiply_two_matrices_brute_force_algorithm import multiply_two_matrices_brute_force_algorithm as multiply_brute_force
from .split_matrix import split_matrix
from .entrywise_sum_two_matrices import entrywise_sum_two_matrices as sum_matrices
from .entrywise_subtract_two_matrices import entrywise_subtract_two_matrices as subtract_matrices
from .get_horizontal_stack import get_horizontal_stack
from .get_vertical_stack import get_vertical_stack


def strassen_with_vanila_python_3(matrix_1: list, matrix_2: list) -> list:
    if len(matrix_1) <= 2:
        return multiply_brute_force(matrix_1, matrix_2)

    a, b, c, d = split_matrix(matrix_1)
    e, f, g, h = split_matrix(matrix_2)

    p1 = strassen_with_vanila_python_3(sum_matrices(a, d), sum_matrices(e, h))
    p2 = strassen_with_vanila_python_3(d, subtract_matrices(g, e))
    p3 = strassen_with_vanila_python_3(sum_matrices(a, b), h)
    p4 = strassen_with_vanila_python_3(subtract_matrices(b, d), sum_matrices(g, h))
    p5 = strassen_with_vanila_python_3(a, subtract_matrices(f, h))
    p6 = strassen_with_vanila_python_3(sum_matrices(c, d), e)
    p7 = strassen_with_vanila_python_3(subtract_matrices(a, c), sum_matrices(e, f))

    c11 = sum_matrices(sum_matrices(p1, subtract_matrices(p2, p3)), p4)
    c12 = sum_matrices(p5, p3)
    c21 = sum_matrices(p6, p2)
    c22 = sum_matrices(p5, subtract_matrices(subtract_matrices(p1, p6), p7))

    result = get_vertical_stack(get_horizontal_stack(c11, c12), get_horizontal_stack(c21, c22))

    return result
