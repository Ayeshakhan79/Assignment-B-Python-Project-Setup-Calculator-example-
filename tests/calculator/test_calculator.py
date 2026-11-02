import unittest
from src.calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 3), 5)


if __name__ == '__main__':
    unittest.main()