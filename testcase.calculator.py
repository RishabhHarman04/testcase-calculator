import calculator
import unittest
class TestCalculator(unittest.TestCase):
    def __setup(self):
        self.x=14
        self.y=10

    def __teardown(self):
        self.x =0
        self.y =0
    def test_add(self):
        result = calculator.add(self.x,self.y)
        self.assertEqual(result, self.x+self.y)
    def test_sub(self):

        result = calculator.sub(self.x,self.y)
        self.assertEqual(result, self.x-self.y)

    def test_mult(self):

        result = calculator.mult(self.x, self.y)
        self.assertEqual(result, self.x*self.y)

    def test_div(self):

        result = calculator.div(self.x,self.y)
        self.assertEqual(result, self.x/self.y)
if __name__ == '__main__':
        unittest.main()
