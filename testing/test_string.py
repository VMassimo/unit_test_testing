import unittest

class TestStringConcatenation(unittest.TestCase):
    def test_concatenation(self):
        result = "Hello, " + "World!"
        self.assertEqual(result, "Hello, World!")

if __name__ == '__main__':
    unittest.main()
