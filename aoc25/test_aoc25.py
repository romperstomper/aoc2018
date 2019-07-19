import unittest
import aoc25
import networkx as nx

class Test25(unittest.TestCase):
    def test_countconstellations(self):
        G=nx.Graph()
        data = aoc25.creategraph(aoc25.DATA0)
        print(data)
        G.add_nodes_from(data)
        self.assertEqual(aoc25.counter(aoc25.DATA0), 2)

if __name__ == '__main__':
    unittest.main()
