"""
unit test
"""

import unittest
import unittestdemo.circle_area as ca
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(ca.circle_area(1), pi * 1 ** 2)
        self.assertAlmostEqual(ca.circle_area(0), 0)
        # self.assertAlmostEqual(ca.circle_area(2.1), pi * 2.1 ** 3)
        self.assertAlmostEqual(ca.circle_area(2), pi * 2 ** 2)

    def test_values(self):
        # make sure value errors are raised when necessary
        self.assertRaises(ValueError, ca.circle_area, -2)

    def test_types(self):
        # make sure type errors are raised when necessary
        self.assertRaises(TypeError, ca.circle_area, 1+2j)
        self.assertRaises(TypeError, ca.circle_area, True)
        self.assertRaises(TypeError, ca.circle_area, "abc")
