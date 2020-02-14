def makecords(data=None):
  allpoints = []
  if not data:
    with open('input') as fd:
      data = fd.read().splitlines()
    for i in data:
      x,y = int(i.split(', ')[0]), int(i.split(', ')[1])
      allpoints.append((x,y))
    return allpoints
  else:
    return data

def makepoints(data=None):
  allpoints = []
  if not data:
    with open('input') as fd:
      data = fd.read().splitlines()
    for i in data:
      x,y = int(i.split(', ')[0]), int(i.split(', ')[1])
      allpoints.append(Point(x,y))
  else:
    for i in data:
      allpoints.append(Point(i[0],i[1]))
  return allpoints

class Point():
  def __init__(self, x, y):
    self.column = x
    self.row = y

  def __repr__(self):
    return '(' + str(self.column) + ', ' + str(self.row) + ')'

  def __sub__(self, other):
    return abs((self.column - other.column) + (self.row - other.row))

  def __ge__(self, other):
    return self.column>=other.column

  def __gt__(self, other):
    return self.column>other.column

  def __lt__(self, other):
    return self.column<other.column

  def __le__(self, other):
    return self.column<=other.column


def isinfinite(self, points):
  pass



def maxcolumn(points):
  return max(points)

def mandist(a, b):
    return

def closest(point):
    pass

