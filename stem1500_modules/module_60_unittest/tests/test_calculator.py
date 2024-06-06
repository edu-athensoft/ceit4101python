import unittest

from stem1500_modules.module_60_unittest.myapp.calculator import *

class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        print("start")

    def tearDown(self) -> None:
        print("teardown")


    def test_init(self):
        c = Calculator(1,2)
        self.assertEqual(c.x, 1)
        self.assertEqual(c.y, 2)

    def test_add(self):
        c = Calculator(3,4)
        result = c.add()
        self.assertEqual(result, 7)




