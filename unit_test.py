

"""
Automatically test all function
    ***currently getting unidentifiable failures***
       todo: looking into that
"""

import unittest
from route import Route


class TestStringMethods(unittest.TestCase):


    def test_findstandardpath(self):
        t = Route("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
        self.assertEqual(t.findstandardpath("A-B-C"), 9)
        self.assertEqual(t.findstandardpath("A-D"), 5)
        self.assertEqual(t.findstandardpath("A-D-C"), 13)
        self.assertEqual(t.findstandardpath("A-E-B-C-D"), 22)
        self.assertEqual(t.findstandardpath("A-E-D"), "NO SUCH ROUTE")

    def test_findtripstoandfroapath(self):
        t = Route("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
        self.assertEqual(t.findtripstoandfroapath("C C", 3, 0), 2)
        self.assertEqual(t.findtripstoandfroapath("A C", 0, 4), 3)

    def test_findshortestpath(self):
        t = Route("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
        self.assertEqual(t.findshortestpath("A C"), 9)
        self.assertEqual(t.findshortestpath("B B"), 9)

    def test_finddifferentpaths(self):
        t = Route("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
        self.assertEqual(t.finddifferentpaths("C C", 30), 7)

if __name__ == '__main__':
    unittest.main()
