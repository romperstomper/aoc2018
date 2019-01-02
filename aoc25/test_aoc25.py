import unittest
import aoc25

class Test25(unittest.TestCase):
    def test_countconstellations(self):
        data = aoc25.readfileinput()
        #self.assertEqual(aoc25.counter(data), 359)
        self.assertEqual(aoc25.counter(aoc25.DATA0), 2)
        #self.assertEqual(aoc25.creategraph(aoc25.DATA0), 2)
        #self.assertEqual(aoc25.creategraph(aoc25.DATA0), 2)

if __name__ == '__main__':
    unittest.main()
