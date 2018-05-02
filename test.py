import unittest
from calculator import Calculator
import math

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        """Tests the add function for every combination of 1, 0 and -1.
        May be redundant but checks if communitive property is respected.
        """

        # Where x = 1
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.add(1, 0), 1)
        self.assertEqual(self.calculator.add(1, -1), 0)

        # Where x = 0
        self.assertEqual(self.calculator.add(0, 1), 1)
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(0, -1), -1)

        # Where x = -1
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, 0), -1)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def test_subtract(self):
        """Tests the subtract function for every combination of 1, 0 and -1.
        May be redundant but checks if communitive property is respected.
        """

        # Where x = 1
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.subtract(1, 0), 1)
        self.assertEqual(self.calculator.subtract(1, -1), 2)

        # Where x = 0
        self.assertEqual(self.calculator.subtract(0, 1), -1)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertEqual(self.calculator.subtract(0, -1), 1)

        # Where x = -1
        self.assertEqual(self.calculator.subtract(-1, 1), -2)
        self.assertEqual(self.calculator.subtract(-1, 0), -1)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        """Tests the multiply function for every combination of 1, 0 and -1.
        May be redundant but checks if communitive property is respected.
        """

        # Where x = 1
        self.assertEqual(self.calculator.multiply(1, 1), 1)
        self.assertEqual(self.calculator.multiply(1, 0), 0)
        self.assertEqual(self.calculator.multiply(1, -1), -1)

        # Where x = 0
        self.assertEqual(self.calculator.multiply(0, 1), 0)
        self.assertEqual(self.calculator.multiply(0, 0), 0)
        self.assertEqual(self.calculator.multiply(0, -1), 0)

        # Where x = -1
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-1, 0), 0)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)

    def test_divide(self):
        """Tests the divide function for every combination of 1, 0 and -1.
        May be redundant but checks if communitive property is respected.

        Note: Since our divide function will throw ZeroDivisionErrors when
        passing a value of 0 for y, you'll notice we use assertRaises to ensure
        that these exceptions are thrown when expected.
        """

        # Where x = 1
        self.assertEqual(self.calculator.divide(1, 1), 1)
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 1, 0)
        self.assertEqual(self.calculator.divide(1, -1), -1)

        # Where x = 0
        self.assertEqual(self.calculator.divide(0, 1), 0)
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 0, 0)
        self.assertEqual(self.calculator.divide(0, -1), 0)

        # Where x = -1
        self.assertEqual(self.calculator.divide(-1, 1), -1)
        self.assertRaises(ZeroDivisionError, self.calculator.divide, -1, 0)
        self.assertEqual(self.calculator.divide(-1, -1), 1)
        
    def test_tan(self):
        """Tests the subtract function for every combination of 1, 0 and -1.
        May be redundant but checks if communitive property is respected.
        """

        # Where x = 1
        self.assertEqual(self.calculator.tan(math.radians(0)), 0)
        # self.assertEqual(self.calculator.tan(math.radians(45)), 1)
        # self.assertEqual(self.calculator.tan(math.radians(80)), 2)

        # Where x = 0
        # self.assertEqual(self.calculator.tan(100), )
        # self.assertEqual(self.calculator.tan(135), )
        # self.assertEqual(self.calculator.tan(180), )

        # Where x = -1
        # self.assertEqual(self.calculator.tan(225), )
        # self.assertEqual(self.calculator.tan(270), )
        # self.assertEqual(self.calculator.tan(360), )

   def test_square(self):
        """Tests the square function for every combination of 1, 0 and -1.
        May be redundant but checks if communitive property is respected.
        """

        # Where x = 1, 0, -1
        self.assertEqual(self.calculator.square(1), 1)
        self.assertEqual(self.calculator.square(0), 0)
        self.assertEqual(self.calculator.square(-1), 1)

       

    def test_log(self):

        self.assertEqual(self.calculator.log(2,10),0.30103)
        self.assertEqual(self.calculator.log(10,10), 1)
        self.assertEqual(self.calculator.log(1,math.exp(1)), 0)

if __name__ == '__main__':
    unittest.main()
