import unittest

class TestEquality(unittest.TestCase):
    def test_equality(self):
        value1 = "abc"
        value2 = "abc"
        self.assertEqual(value1, value2)

if __name__ == '__main__':
    unittest.main()
