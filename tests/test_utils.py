"""
unittest for utils module
"""
import unittest

from math_so.utils import say_hello_world, absolute_error, relative_error, signif, positional2decimal


class TestUtils(unittest.TestCase):

    """ Test Main Helper Function """

    def test_main(self):
        """ Test Utility Function Print Statement """

        self.assertEqual(say_hello_world(), "Hello World!")
        self.assertEqual(absolute_error(5, 4.9), 5-4.9)
        self.assertEqual(relative_error(5, 4.9), (5-4.9)/5)
        self.assertEqual(signif(123.45, 4), 123.4)
        self.assertEqual(signif(0.0012345, 3), 0.00123)
        self.assertEqual(signif(-1234.5, 3), -1230.0)
        self.assertEqual(signif(0, 3), 0.0)
        self.assertEqual(positional2decimal('1.1', 16), 1+1/16)


if __name__ == '__main__':
    unittest.main()
