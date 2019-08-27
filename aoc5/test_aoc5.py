import aoc5
import unittest

class Testaoc5(unittest.TestCase):
    def test_parser(self):
        #self.assertEqual(aoc5.parser('dabAcCaCBAcCcaDA'),'dabCBAcaDA')
        self.assertEqual(aoc5.parser('abBA'),'')
        self.assertEqual(aoc5.parser('abAB'),'abAB')

if __name__ == '__main__':
    unittest.main()
