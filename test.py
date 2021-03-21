
"""
Manually confirm all answers given
"""

from route import Route


def maintest():
    # t = Route("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
    t = Route()
    t.findstandardpath("A-B-C")
    t.findstandardpath("A-D")
    t.findstandardpath("A-D-C")
    t.findstandardpath("A-E-B-C-D")
    t.findstandardpath("A-E-D")
    t.findtripstoandfroapath("C C", 3, 0)
    t.findtripstoandfroapath("A C", 0, 4)
    t.findshortestpath("A C")
    t.findshortestpath("B B")
    t.finddifferentpaths("C C", 30)


if __name__ == '__main__':
    maintest()
