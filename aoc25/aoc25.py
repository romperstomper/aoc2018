from collections import namedtuple
import itertools
import pdb
from collections import deque
DATA0 = [
[0,0,0,0],
[3,0,0,0],
[0,3,0,0],
[0,0,3,0],
[0,0,0,3],
[0,0,0,6],
[9,0,0,0],
[12,0,0,0]
]
DATA=[
[0,0,0,6],
[9,0,0,0],
[12,0,0,0]
]
def readfileinput():
    result = list()
    with open('input') as fd:
        data = fd.read().splitlines()
    for line in data:
        result.append(list(map(int, line.split(','))))
    return formatter(result)

def creategraph(cords):
    result = []
    edges = [set() for _ in range(len(cords))]
    for i,(w,x,y,z) in enumerate(cords):
        for j,(w2,x2,y2,z2) in enumerate(cords):
            if (abs(w - w2)+abs(x - x2)+abs(y - y2)+abs(z - z2) <=3):
                edges[i].add(j)
                #print(cords[i],cords[j],abs(w - w2)+abs(x - x2)+abs(y - y2)+abs(z - z2))
            #else:
                #print(cords[i],cords[j],abs(w - w2)+abs(x - x2)+abs(y - y2)+abs(z - z2))
    return edges

def counter(cords):
    graph = creategraph(cords)
    Set = set()
    ans = 0
    l = len(cords)
    for i in range(l):
        if i in Set:
            continue
        ans +=1
        Q = deque()
        Q.append(i)
        while Q:
            x = Q.popleft()
            if x in Set:
                continue
            Set.add(x)
            for y in graph[x]:
                Q.append(y)
    return ans

def formatter(data):
    result = list()
    for line in data:
        w,x,y,z = line
        result.append((w,x,y,z))
    return result
DATA2 = [
[-1,2,2,0],
[0,0,2,-2],
[0,0,0,-2],
[-1,2,0,0],
[-2,-2,-2,2],
[3,0,2,-1],
[-1,3,2,2],
[-1,0,-1,0],
[0,2,1,-2],
[3,0,0,0],
]          
DATA3=[
[1,-1,0,1],
[2,0,-1,0],
[3,2,-1,0],
[0,0,3,1],
[0,0,-1,-1],
[2,3,-2,0],
[-2,2,0,0],
[2,-2,0,-1],
[1,-1,0,-1],
[3,2,0,2]
]
