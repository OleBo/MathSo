import unittest

from math_so import utils


class TestUtils(unittest.TestCase):

    """ Test Main Helper Function """

    def test_main(self):
        """ Test Utility Function Print Statement """

        self.assertEqual(utils.say_hello_world(), "Hello World!")
