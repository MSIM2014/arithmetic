import arithmetic
import unittest

class TestArithmetic(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(arithmetic.add(1,2), 3)

    def test_subtraction(self):
        self.assertEqual(arithmetic.subtract(2, 1), 1)

    def test_division(self):
        self.assertEqual(arithmetic.divide(8, 2), 4)

if __name__ == '__main__':
    unittest.main()
