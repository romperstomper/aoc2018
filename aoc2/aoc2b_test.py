import aoc2b
import unittest

class Testaoc2b(unittest.TestCase):
    def test_count_both(self):
        self.assertEqual(aoc2.count(['bababc']), (1,1))


if __name__ == '__main__':
    unittest.main()
