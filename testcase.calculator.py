import calculator
import unittest
class TestCalculator(unittest.TestCase):
    def test_add(self):
        x=10
        y=20
        result = calculator.add(x,y)
        self.assertEqual(result, x+y)
    def test_sub(self):
        x=10
        y=20
        result = calculator.sub(x,y)
        self.assertEqual(result, x-y)

    def test_mult(self):
        x = 10
        y = 20
        result = calculator.mult(x, y)
        self.assertEqual(result, x*y)

    def test_div(self):
        x = 10
        y = 20
        result = calculator.div(x, y)
        self.assertEqual(result, x/y)
if __name__ == '__main__':
        unittest.main()
