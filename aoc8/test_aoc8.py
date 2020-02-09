import unittest
import aoc8

class Test_aoc8(unittest.TestCase):
    def test_metatree(self):
        self.assertEqual(aoc8.metatree(), 138)


if __name__ == '__main__':
    unittest.main()
