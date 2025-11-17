import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(-1,1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-2, 4), -8)

    def test_divide(self):
        self.assertEqual(calculator.div(10, 2), 5)
        self.assertEqual(calculator.div(-9, 3), -3)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)
        with self.assertRaises(ValueError):
            calculator.logarithm(5, -2)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
        self.assertAlmostEqual(calculator.square_root(4), 2.0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
