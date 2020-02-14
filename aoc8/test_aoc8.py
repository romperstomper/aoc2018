import unittest
import aoc8

class Test_aoc8(unittest.TestCase):
    def test_metatree(self):
        smallinput = iter([int(x) for x in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')])
        a8 = aoc8.Aoc8()
        smallresult = a8.metatree(smallinput)
        self.assertEqual(a8.total(smallresult), 138)


if __name__ == '__main__':
    unittest.main()
