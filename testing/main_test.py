import unittest
import glob

def run_tests():
    test_files = glob.glob("test_*.py")  # Assumes your test files are named with a prefix "test_"

    suite = unittest.TestLoader().discover(".", pattern="test_*.py")

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()

    if not success:
        exit(1)  # Exit with a non-zero status code if tests fail
