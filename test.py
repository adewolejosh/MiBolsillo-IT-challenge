from route import Route


def maintest():
    t = Route()
    # t.findtripstoandfroapath("A C", "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
    t.findshortestpath("A C")


if __name__ == '__main__':
    maintest()