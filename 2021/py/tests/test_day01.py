import unittest

class TestFileContains567(unittest.TestCase):
    def test_file_contains_567(self):
        with open("tests/input/day01.txt", "r") as f:
            for line in f:
                self.assertEqual(line.strip(), "200")

if __name__ == "__main__":
    unittest.main()
