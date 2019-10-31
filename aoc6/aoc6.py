import pdb
from collections import defaultdict
def readinput():
  allpoints = []
  with open('input') as fd:
    data = fd.read().splitlines()
  for i in data:
    x,y = int(i.split(', ')[0]), int(i.split(', ')[1])
    allpoints.append((x,y))
  return allpoints

data = readinput()
#data=[(1,1),(1,6),(8,3),(3,4),(5,5),(8,9)]
x0 = sorted(data)[0][0]
xn = sorted(data)[-1][0]
y0 = sorted(data,key=lambda x:x[1])[0][1]
yn = sorted(data,key=lambda x:x[1])[-1][1]


def mandist(source, dest):
  return abs(source[0] - dest[0]) + abs(source[1] - dest[1])

infinite = set()
count = defaultdict(int)
def walk():
  for x in range(x0, xn+1):
    for y in range(y0, yn+1):
      dists = sorted((mandist((x,y), point), point) for point in data)
      if dists[0][0] != dists[1][0]:
        count[dists[0][1]] +=1
        if x == x0 or x==xn or y == y0 or y == yn:
          infinite.add(dists[0][1])
walk()
for k in infinite:
  count.pop(k)

print(max(count.values()))
      
