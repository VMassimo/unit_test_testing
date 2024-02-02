import unittest

def is_string_reversed(input_str):
    # Check if the input string is equal to its reverse
    return input_str == input_str[::-1]

class TestStringReversal(unittest.TestCase):
    def test_reversed_string(self):
        self.assertTrue(is_string_reversed("radar"))  # Example of a palindrome
        self.assertTrue(is_string_reversed("level"))
        self.assertTrue(is_string_reversed("madam"))
        self.assertFalse(is_string_reversed("hello"))
        self.assertFalse(is_string_reversed("world"))

if __name__ == '__main__':
    unittest.main()
