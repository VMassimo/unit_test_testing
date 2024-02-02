import unittest

class TestDivision(unittest.TestCase):
    def test_division(self):
        result = 10 / 2
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
