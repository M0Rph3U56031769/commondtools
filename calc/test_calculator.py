import unittest

import calc.calculator


class BasicTestSuite(unittest.TestCase):
    def test_something(self):
        self.assertEqual(calc.calculator.Calculator.get_average([1, 2]), 1.5)


if __name__ == '__main__':
    unittest.main()
