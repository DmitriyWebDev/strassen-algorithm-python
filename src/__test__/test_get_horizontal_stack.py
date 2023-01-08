import unittest
from ..get_horizontal_stack import get_horizontal_stack


class MyTestCase(unittest.TestCase):
    def test_get_horizontal_stack(self):
        matrix_a = [
            [37, 23],
            [36, 25]
        ]
        matrix_b = [
            [32, 53],
            [42, 37]
        ]
        matrix_result = [
            [37, 23, 32, 53],
            [36, 25, 42, 37]
        ]

        self.assertEqual(get_horizontal_stack(matrix_a, matrix_b), matrix_result)


if __name__ == '__main__':
    unittest.main()
