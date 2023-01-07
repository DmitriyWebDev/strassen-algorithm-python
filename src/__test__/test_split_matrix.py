import unittest
from ..split_matrix import split_matrix


class MyTestCase(unittest.TestCase):
    def test_split_matrix(self):
        matrix_a = [
            [3, 5, 1, 3],
            [1, 2, 3, 4],
            [4, 5, 6, 8],
            [7, 8, 9, 3]
        ]
        result_a = [
            [[3, 5], [1, 2]],
            [[1, 3], [3, 4]],
            [[4, 5], [7, 8]],
            [[6, 8], [9, 3]]
        ]

        self.assertEqual(split_matrix(matrix_a), result_a)


if __name__ == '__main__':
    unittest.main()
