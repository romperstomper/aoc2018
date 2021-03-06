import unittest
import aoc3

EXPECTED=(
        [(437, 811), (437, 812), (437, 813), (437, 814), (437, 815), (437, 816), (437, 817), (437, 818), (437, 819), (437, 820), (438, 811), (438, 812), (438, 813), (438, 814), (438, 815), (438, 816), (438, 817), (438, 818), (438, 819), (438, 820), (439, 811), (439, 812), (439, 813), (439, 814), (439, 815), (439, 816), (439, 817), (439, 818), (439, 819), (439, 820), (440, 811), (440, 812), (440, 813), (440, 814), (440, 815), (440, 816), (440, 817), (440, 818), (440, 819), (440, 820), (441, 811), (441, 812), (441, 813), (441, 814), (441, 815), (441, 816), (441, 817), (441, 818), (441, 819), (441, 820), (442, 811), (442, 812), (442, 813), (442, 814), (442, 815), (442, 816), (442, 817), (442, 818), (442, 819), (442, 820), (443, 811), (443, 812), (443, 813), (443, 814), (443, 815), (443, 816), (443, 817), (443, 818), (443, 819), (443, 820), (444, 811), (444, 812), (444, 813), (444, 814), (444, 815), (444, 816), (444, 817), (444, 818), (444, 819), (444, 820), (445, 811), (445, 812), (445, 813), (445, 814), (445, 815), (445, 816), (445, 817), (445, 818), (445, 819), (445, 820), (446, 811), (446, 812), (446, 813), (446, 814), (446, 815), (446, 816), (446, 817), (446, 818), (446, 819), (446, 820), (447, 811), (447, 812), (447, 813), (447, 814), (447, 815), (447, 816), (447, 817), (447, 818), (447, 819), (447, 820), (448, 811), (448, 812), (448, 813), (448, 814), (448, 815), (448, 816), (448, 817), (448, 818), (448, 819), (448, 820), (449, 811), (449, 812), (449, 813), (449, 814), (449, 815), (449, 816), (449, 817), (449, 818), (449, 819), (449, 820), (450, 811), (450, 812), (450, 813), (450, 814), (450, 815), (450, 816), (450, 817), (450, 818), (450, 819), (450, 820), (451, 811), (451, 812), (451, 813), (451, 814), (451, 815), (451, 816), (451, 817), (451, 818), (451, 819), (451, 820), (452, 811), (452, 812), (452, 813), (452, 814), (452, 815), (452, 816), (452, 817), (452, 818), (452, 819), (452, 820), (453, 811), (453, 812), (453, 813), (453, 814), (453, 815), (453, 816), (453, 817), (453, 818), (453, 819), (453, 820), (454, 811), (454, 812), (454, 813), (454, 814), (454, 815), (454, 816), (454, 817), (454, 818), (454, 819), (454, 820), (455, 811), (455, 812), (455, 813), (455, 814), (455, 815), (455, 816), (455, 817), (455, 818), (455, 819), (455, 820)])
class Testaoc3(unittest.TestCase):
    #1 @ 1,3: 4x4
    @unittest.skip
    def test_cords(self):
        self.assertEqual(aoc3.cords('#1 @ 1,3: 4x4'), ((1,3), (4,4))) 

    @unittest.skip
    def test_readinput(self):
        self.assertEqual(aoc3.readinput(), None)

    @unittest.skip
    def test_last_cords(self):
        z = aoc3.readinput().pop()
        self.assertEqual(aoc3.cords(z), ((437,811), (19,10))) 

    @unittest.skip
    def test_gen_cords(self):
        z = aoc3.readinput().pop()
        self.assertEqual(aoc3.gen_cords(z), EXPECTED)

    @unittest.skip
    def test_ddict(self):
        self.assertEqual(aoc3.ddict(), None)

    def test_leftover(self):
        self.assertEqual(aoc3.leftover(), None)

