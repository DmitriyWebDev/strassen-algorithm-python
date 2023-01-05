import unittest
from ..index import my_function


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(my_function('1'), "1 Refsnes", "Should be - 1 Refsnes")


if __name__ == '__main__':
    unittest.main()
