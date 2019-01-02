import unittest
import aoc25

class Test25(unittest.TestCase):
    def test_checkrange(self):
        data = aoc25.DATA
        self.assertEqual(aoc25.manhattan(data[0], data[1]), False)
        self.assertTrue(aoc25.manhattan(data[1], data[2]), True)

    def est_countconstellations(self):
        pass
        #res = aoc25.countconstellations(aoc25.DATA)

if __name__ == '__main__':
    unittest.main()
