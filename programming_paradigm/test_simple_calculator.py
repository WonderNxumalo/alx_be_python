import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class, covering addition, subtraction,
    multiplication, and division operations and their respective edge cases.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

# -------------------------- Addition Tests --------------------------

    def test_addition(self):
        """Test the add method with positive, negative, and zero inputs."""
        # Normal positive addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(100, 200), 300)

        # Addition with negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-5, 10), 5)

        # Addition with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(-5, 0), -5)

# ------------------------ Subtraction Tests -------------------------

    def test_subtraction(self):
        """Test the subtract method with various positive and negative numbers."""
        # Normal positive subtraction
        self.assertEqual(self.calc.subtract(10, 3), 7)

        # Subtraction resulting in a negative number
        self.assertEqual(self.calc.subtract(5, 15), -10)

        # Subtraction with negative numbers
        self.assertEqual(self.calc.subtract(-10, -5), -5) # -10 - (-5) = -5
        self.assertEqual(self.calc.subtract(5, -5), 10)   # 5 - (-5) = 10

        # Subtraction with zero
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 10), -10)

# ----------------------- Multiplication Tests -----------------------

    def test_multiplication(self):
        """Test the multiply method with positive, negative, and zero inputs."""
        # Normal positive multiplication
        self.assertEqual(self.calc.multiply(4, 5), 20)

        # Multiplication with negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-4, -5), 20)

        # Multiplication by one
        self.assertEqual(self.calc.multiply(10, 1), 10)

        # Multiplication by zero (Edge Case)
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)


# -------------------------- Division Tests --------------------------

    def test_division_normal(self):
        """Test the divide method with normal, non-zero results."""
        # Standard integer division
        self.assertEqual(self.calc.divide(10, 2), 5.0)

        # Division resulting in a float
        self.assertEqual(self.calc.divide(10, 4), 2.5)

        # Division with negative numbers
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)

    def test_division_by_zero_edge_case(self):
        """Test the critical edge case of division by zero."""
        # The SimpleCalculator divide method returns None if b == 0
        self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None")
        self.assertIsNone(self.calc.divide(0, 0), "Division by zero should return None")


if __name__ == '__main__':
    # Running the tests using the command line is the preferred method
    # python -m unittest test_simple_calculator.py
    unittest.main()