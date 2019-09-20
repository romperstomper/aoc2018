import aoc6
import unittest

class Testaoc6(unittest.TestCase):
    def test_points(self):
        pointa = aoc6.Point(1, 1)
        pointb = aoc6.Point(1, 6)
        self.assertEqual((pointa - pointb),5)

    def test_makepoints(self):
        self.assertEqual(aoc6.makepoints()[0].x, 336)

if __name__ == '__main__':
    unittest.main()
