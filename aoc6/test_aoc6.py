import aoc6
import unittest

class Testaoc6(unittest.TestCase):
  
  def setUp(self):
    self.cords = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]

  def test_points(self):
    pointa = aoc6.Point(1, 1)
    pointb = aoc6.Point(1, 6)
    self.assertEqual((pointa - pointb),5)

  def test_makepoints(self):
    self.assertEqual(aoc6.makepoints()[0].column, 336)

  def test_maxcolumns(self):
    points = aoc6.makepoints(self.cords)
    self.assertEqual(aoc6.maxcolumn(points).column, 8)
    
  def test_maxrows(self):
    result = max(self.cords, key=lambda item:item[1])[1]
    self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()
