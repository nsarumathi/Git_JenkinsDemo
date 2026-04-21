import unittest
from app import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a new Calculator instance before each test."""
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-2, 4), -8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """Verify that ZeroDivision raises a ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
