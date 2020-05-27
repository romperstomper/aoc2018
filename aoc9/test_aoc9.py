import aoc9
import unittest

class TestAoc9(unittest.TestCase):
    def test_get_score(self):
        self.assertEqual(aoc9.get_score(9, 23), 32)

if __name__ == '__main__':
    unittest.main()
