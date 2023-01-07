import unittest
from ..entrywise_subtract_two_matrices import entrywise_subtract_two_matrices


class MyTestCase(unittest.TestCase):
    def test_entrywise_subtract_two_matrices(self):
        matrix_a = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        matrix_b = [
            [7, 8, 9],
            [10, 11, 3]
        ]
        matrix_result = [
            [-6, -6, -6],
            [-6, -6, 3]
        ]

        self.assertEqual(entrywise_subtract_two_matrices(matrix_a, matrix_b), matrix_result)


if __name__ == '__main__':
    unittest.main()
