import aoc4
import unittest

class Testaoc4(unittest.TestCase):
  def test1(self):
    dates = [
        "[1518-11-22 00:49]",
        "[1518-05-18 00:01]",
        "[1518-11-20 00:28]",
        "[1518-10-27 00:37]"
    ]
    dates = [aoc4.datetime.strptime(x[1:17], '%Y-%m-%d %H:%M') for x in dates]
    dates.sort()
    self.assertEqual(aoc4.order(), dates)


if __name__ == '__main__':
  unittest.main()
