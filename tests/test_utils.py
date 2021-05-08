"""
unittest for utils module
"""
import math
import unittest
import numpy as np

from math_so.utils import (say_hello_world, absolute_error, relative_error,
                           signif, positional2decimal, bisection, newton,
                           heron, secant_method, regula_falsi, fpiterate)


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

    def test_nonlinear(self):
        """ Test Utility Function Nonlinear Systems """

        self.assertEqual(bisection(lambda x: np.exp(-x) - np.sin(x), 0,
                                   .5*math.pi, 1e-6), 0.5885329263701276)
        self.assertEqual(newton(lambda x: np.exp(-x) - np.sin(x),
                                lambda x: -np.exp(-x) - np.cos(x), 1., 1e-6),
                         0.5885327439818611)
        self.assertEqual(heron(4, 1e-6), 2.000000000000002)
        self.assertEqual(secant_method(lambda x: np.exp(-x) - np.sin(x),
                                       .7, 1., 1e-6), 0.5885327496049312)
        self.assertEqual(regula_falsi(lambda x: np.exp(-x) - np.sin(x),
                                      0, .5*math.pi, 1e-6), 0.5885328238248644)
        self.assertEqual(fpiterate(lambda x: np.arcsin(np.exp(-x)), 1., 1e-6),
                         0.588533120227473)


if __name__ == '__main__':
    unittest.main()
