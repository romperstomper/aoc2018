import unittest
import aoc8

class Test_aoc8(unittest.TestCase):
    def test_metatree(self):
        input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')
        self.assertEqual(aoc8.metatree(input), 138)


if __name__ == '__main__':
    unittest.main()
