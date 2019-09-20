class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __sub__(self, other):
        return abs((self.x - other.x) + (self.y - other.y))

def makepoints():
    with open('input') as fd:
        data = fd.read().splitlines()
    allpoints = []
    for i in data:
        x,y = int(i.split(', ')[0]), int(i.split(', ')[1])
        allpoints.append(Point(x,y))
    return allpoints


def mandist(a, b):
    return

def closest(point):
    pass
