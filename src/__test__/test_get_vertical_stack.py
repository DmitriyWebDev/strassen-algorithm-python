import unittest
from ..get_vertical_stack import get_vertical_stack


class MyTestCase(unittest.TestCase):
    def test_get_vertical_stack(self):
        matrix_a = [
            [37, 23, 32, 53],
            [36, 25, 42, 37]
        ]
        matrix_b = [
            [81, 54, 89, 86],
            [72, 65, 91, 99]
        ]
        matrix_result = [
            [37, 23, 32, 53],
            [36, 25, 42, 37],
            [81, 54, 89, 86],
            [72, 65, 91, 99]
        ]

        self.assertEqual(get_vertical_stack(matrix_a, matrix_b), matrix_result)


if __name__ == '__main__':
    unittest.main()
