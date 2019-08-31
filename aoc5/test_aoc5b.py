import aoc5b
import unittest

class Testaoc5(unittest.TestCase):
    def test_parser(self):
        ""
        #self.assertEqual(aoc5.parser('dabAcCaCBAcCcaDA'),'daDA')
        #self.assertEqual(aoc5.parser('abBA'),'')
        #self.assertEqual(aoc5.parser('abAB'),'abAB')

    def test_transform(self):
        self.assertEqual(aoc5b.transform('c', 'dabAcCaCBAcCcaDA'),'daDA')
        #self.assertEqual(aoc5.parser('abBA'),'')
if __name__ == '__main__':
    unittest.main()
