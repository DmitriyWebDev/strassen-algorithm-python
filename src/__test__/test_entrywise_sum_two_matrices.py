import unittest
from ..entrywise_sum_two_matrices import entrywise_sum_two_matrices


class MyTestCase(unittest.TestCase):
    def test_entrywise_sum_two_matrices(self):
        matrix_a = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        matrix_b = [
            [7, 8, 9],
            [10, 11, 12]
        ]
        matrix_result = [
            [8, 10, 12],
            [14, 16, 18]
        ]

        self.assertEqual(entrywise_sum_two_matrices(matrix_a, matrix_b), matrix_result)


if __name__ == '__main__':
    unittest.main()
