import unittest

class TestListLength(unittest.TestCase):
    def test_length(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(len(my_list), 5)

if __name__ == '__main__':
    unittest.main()
