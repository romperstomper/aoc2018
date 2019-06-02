import aoc4
import unittest

class Testaoc4(unittest.TestCase):
  def test1(self):
    expected = [
        '[1518-03-07 00:02] Guard #1291 begins shift', 
        '[1518-03-07 00:19] falls asleep'
        ]
    self.assertEqual(aoc4.readinput()[:2], expected)

  def test_create_guards(self):
      expected = ['1291', '773', '863', '3191', '2791', '2749', '2539', '3257', '269', '3557', '1237', '2251', '631', '1367', '677', '433', '3041', '449', '1873', '2699', '1171', '3019', '239']
      self.assertEqual(list(aoc4.create_guards().keys()), expected)


if __name__ == '__main__':
  unittest.main()
