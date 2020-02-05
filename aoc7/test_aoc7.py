import unittest
import aoc7

class TestAoc7(unittest.TestCase):
  def test_steps(self):
    s = """Step C must be finished before step A can begin.
    Step C must be finished before step F can begin.
    Step A must be finished before step B can begin.
    Step A must be finished before step D can begin.
    Step B must be finished before step E can begin.
    Step D must be finished before step E can begin.
    Step F must be finished before step E can begin."""
 import   expected = "CABDFE"

    self.assertEqual(aoc7.parse(s), expected)

if __name__ == "__main__":
  unittest.main()
