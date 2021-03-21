from route import Route


def maintest():
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