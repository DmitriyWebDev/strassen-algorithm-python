import unittest
from ..get_normalized_matrices import get_normalized_matrices


class MyTestCase(unittest.TestCase):
    def test_check_valid_matrices(self):
        matrix_a = [
            [1, 2, 3, 8],
            [4, 5, 6, 0],
            [37, 23, 32, 53],
            [36, 25, 42, 37]
        ]
        matrix_b = [
            [7, 8, 9, 7],
            [10, 11, 12, 88],
            [1, 2, 3, 8],
            [4, 5, 6, 0],
        ]
        matrix_a_result = matrix_a
        matrix_b_result = matrix_b

        self.assertEqual(get_normalized_matrices(matrix_a, matrix_b), (matrix_a_result, matrix_b_result))

    def test_check_invalid_matrices_1(self):
        matrix_a = [
            [1, 2, 3, 8],
            [4, 5, 6, 0],
            [37, 23, 32, 53],
        ]
        matrix_b = [
            [7, 8, 9, 7],
            [10, 11, 12, 88],
            [1, 2, 3, 8],
            [4, 5, 6, 0],
        ]
        matrix_a_result = [
            [1, 2, 3, 8],
            [4, 5, 6, 0],
            [37, 23, 32, 53],
            [0, 0, 0, 0]
        ]
        matrix_b_result = matrix_b

        self.assertEqual(get_normalized_matrices(matrix_a, matrix_b), (matrix_a_result, matrix_b_result))

    def test_check_invalid_matrices_2(self):
        matrix_a = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        matrix_b = [
            [2, 2],
        ]
        matrix_a_result = matrix_a
        matrix_b_result = [
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

        self.assertEqual(get_normalized_matrices(matrix_a, matrix_b), (matrix_a_result, matrix_b_result))

    def test_check_invalid_matrices_3(self):
        matrix_a = [
            [1],
        ]
        matrix_b = [
            [2],
        ]
        matrix_a_result = [
            [1, 0],
            [0, 0],
        ]
        matrix_b_result = [
            [2, 0],
            [0, 0],
        ]

        self.assertEqual(get_normalized_matrices(matrix_a, matrix_b), (matrix_a_result, matrix_b_result))

    def test_check_invalid_matrices_4(self):
        matrix_a = [
            [],
        ]
        matrix_b = [
            [],
        ]
        matrix_a_result = [
            [0, 0],
            [0, 0],
        ]
        matrix_b_result = [
            [0, 0],
            [0, 0],
        ]

        self.assertEqual(get_normalized_matrices(matrix_a, matrix_b), (matrix_a_result, matrix_b_result))


if __name__ == '__main__':
    unittest.main()
