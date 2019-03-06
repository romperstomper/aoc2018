import aoc2
import unittest

class Testaoc2(unittest.TestCase):
    real = aoc2.read()
    def test_count_both(self):
        self.assertEqual(aoc2.count(['bababc']), (1,1))

    def test_count_single(self):
        self.assertEqual(aoc2.count(['abbcde']), (1,0))

    def test_count_triple(self):
        self.assertEqual(aoc2.count(['abcccd']), (0,1))

    def test_count_repeat(self):
        self.assertEqual(aoc2.count(['aabcdd']), (1,0))

    def test_count_repeat(self):
        self.assertEqual(aoc2.count(aoc2.read()), (1,0))


if __name__ == '__main__':
    unittest.main()
