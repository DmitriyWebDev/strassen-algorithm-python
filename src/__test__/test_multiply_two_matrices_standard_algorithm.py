import unittest
from ..multiply_two_matrices_standard_algorithm import multiply_two_matrices_standard_algorithm


class MyTestCase(unittest.TestCase):
    def test_multiply_two_matrices_brute_force_algorithm(self):
        matrix_a = [
            [3, 5, 1, 3],
            [1, 2, 3, 4],
            [4, 5, 6, 8],
            [7, 8, 9, 3]
        ]
        matrix_b = [
            [4, 1, 2, 3],
            [1, 2, 1, 6],
            [2, 4, 6, 2],
            [6, 2, 5, 4]
        ]
        matrix_result = [
            [37, 23, 32, 53],
            [36, 25, 42, 37],
            [81, 54, 89, 86],
            [72, 65, 91, 99]
        ]

        self.assertEqual(multiply_two_matrices_standard_algorithm(matrix_a, matrix_b), matrix_result)


if __name__ == '__main__':
    unittest.main()
