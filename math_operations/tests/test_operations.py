import unittest

from basic.add import add
from basic.subtract import subtract
from advanced.multiply import multiply
from advanced.divide import divide
from advanced.exponent import exponent
from advanced.square_root import square_root

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiplication(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8)
        self.assertEqual(exponent(5, 0), 1)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-4)

if __name__ == '__main__':
    unittest.main()

    