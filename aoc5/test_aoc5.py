import aoc5
import unittest

class Testaoc5(unittest.TestCase):
    def test_reader(self):
        self.assertEqual(aoc5.reader(),None)

if __name__ == '__main__':
    unittest.main()
