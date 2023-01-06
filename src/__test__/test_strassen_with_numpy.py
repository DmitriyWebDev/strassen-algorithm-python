import unittest

from numpy import array

from ..strassen_with_numpy import strassen_with_numpy, split
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_strassen_with_numpy(self):
        matrix_a = np.array([
            [3, 5, 1, 3],
            [1, 2, 3, 4],
            [4, 5, 6, 8],
            [7, 8, 9, 3]
        ])
        matrix_b = np.array([
            [4, 1, 2, 3],
            [1, 2, 1, 6],
            [2, 4, 6, 2],
            [6, 2, 5, 4]
        ])
        matrix_result = np.array([
            [37, 23, 32, 53],
            [36, 25, 42, 37],
            [81, 54, 89, 86],
            [72, 65, 91, 99]
        ])

        # https://stackoverflow.com/questions/3302949/best-way-to-assert-for-numpy-array-equality
        np.testing.assert_array_equal(strassen_with_numpy(matrix_a, matrix_b), matrix_result)

    def test_split(self):
        matrix_a = np.array([
            [3, 5, 1, 3],
            [1, 2, 3, 4],
            [4, 5, 6, 8],
            [7, 8, 9, 3]
        ])
        result = (
            array([[3, 5], [1, 2]]),
            array([[1, 3], [3, 4]]),
            array([[4, 5], [7, 8]]),
            array([[6, 8], [9, 3]])
        )

        np.testing.assert_array_equal(split(matrix_a), result)


if __name__ == '__main__':
    unittest.main()
