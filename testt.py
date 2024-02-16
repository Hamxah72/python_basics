# Import the unittest module
import unittest

# Define a class for your test cases
class TestMyFunction(unittest.TestCase):

    # Define a test method with a descriptive name
    def test_my_function_with_positive_numbers(self):
        # Set up test data
        x = 5
        y = 3

        # Call the function you want to test
        result = my_function(x, y)

        # Use an assertion method to check the result
        self.assertEqual(result, 8, "The function should return the sum of the numbers")

# Run the tests
if __name__ == "__main__":
    unittest.main()
