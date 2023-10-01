import unittest

# Import the conversion functions from your script
from src.converter import (
    single_dollar_to_parentheses,
	parentheses_to_single_dollar,
	double_dollar_to_braces,
	braces_to_double_dollar,
)

class TestConverter(unittest.TestCase):
    def test_single_dollar_to_parentheses(self):
        self.assertEqual(single_dollar_to_parentheses('This is $some$ text.'), 'This is \\(some\\) text.')
        self.assertEqual(single_dollar_to_parentheses('$x^2$ is a quadratic function.'), '\\(x^2\\) is a quadratic function.')
        self.assertEqual(single_dollar_to_parentheses('No dollars here.'), 'No dollars here.')

    def test_parentheses_to_single_dollar(self):
        self.assertEqual(parentheses_to_single_dollar('This is \\(some\\) text.'), 'This is $some$ text.')
        self.assertEqual(parentheses_to_single_dollar('\\(x^2\\) is a quadratic function.'), '$x^2$ is a quadratic function.')
        self.assertEqual(parentheses_to_single_dollar('No parentheses here.'), 'No parentheses here.')

    def test_double_dollar_to_braces(self):
        self.assertEqual(double_dollar_to_braces('This is $$some$$ text.'), 'This is \\[some\\] text.')
        self.assertEqual(double_dollar_to_braces('$$x^2$$ is a quadratic function.'), '\\[x^2\\] is a quadratic function.')
        self.assertEqual(double_dollar_to_braces('No double dollars here.'), 'No double dollars here.')

    def test_braces_to_double_dollar(self):
        self.assertEqual(braces_to_double_dollar('This is \\[some\\] text.'), 'This is $$some$$ text.')
        self.assertEqual(braces_to_double_dollar('\\[x^2\\] is a quadratic function.'), '$$x^2$$ is a quadratic function.')
        self.assertEqual(braces_to_double_dollar('No braces here.'), 'No braces here.')

if __name__ == '__main__':
    unittest.main()

