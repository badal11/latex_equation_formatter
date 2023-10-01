import unittest

# Import the conversion functions from your script
from converter import (
    single_dollar_to_parentheses,
	parentheses_to_single_dollar,
	double_dollar_to_braces,
	braces_to_double_dollar,
)

class TestLatexConversion(unittest.TestCase):

    def test_single_dollar_conversion(self):
        input_latex = "This is a $sample$ equation."
        expected_output = "This is a \\(sample\\) equation."
        self.assertEqual(single_dollar_to_parentheses(input_latex), expected_output)

    def test_single_dollar_conversion_back(self):
        input_latex = "This is a \\(sample\\) equation."
        expected_output = "This is a $sample$ equation."
        self.assertEqual(parentheses_to_single_dollar(input_latex), expected_output)

    def test_double_dollar_conversion(self):
        input_latex = "This is a $$displayed$$ equation."
        expected_output = "This is a \\[displayed\\] equation."
        self.assertEqual(double_dollar_to_braces(input_latex), expected_output)

    def test_double_dollar_conversion_back(self):
        input_latex = "This is a \\[displayed\\] equation."
        expected_output = "This is a $$displayed$$ equation."
        self.assertEqual(braces_to_double_dollar(input_latex), expected_output)

if __name__ == '__main__':
    unittest.main()
