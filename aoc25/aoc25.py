from collections import namedtuple
import itertools
import pdb
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
]
def readfileinput():
    cords = namedtuple("Cords", ['w', 'x', 'y', 'z'])

    result = list()
    with open('input') as fd:
        data = fd.read().splitlines()
    for line in data:
        result.append(list(map(int, cords(*line.split(',')))))
    return formatter(result)

def manhattan(a, b):
    w,x,y,z = a
    w2,x2,y2,z2 = b
    if abs(w - w2) <=3 or abs(x - x2) <=3 or abs(y - y2) <=3 or abs(z - z2) <=3:
        print(abs(w - w2) <=3, abs(x - x2) <=3, abs(y - y2) <=3, abs(z - z2)<=3)
        print(abs(w - w2), abs(x - x2) <=3, abs(y - y2) <=3, abs(z - z2)<=3)
        return True
    return False

def countconstellations(cords):
    cords = formatter(cords)
    result = []
    for cord in cords:
        tmplist = []
        result.append(tmplist)
        for i in cords:
            #pdb.set_trace()
            if manhattan(cord, i):
                raise
                tmplist.append(i)
    
    return result

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
[3,0,0,0 ],
]          
DATA3=[
[1,-1,0,1],
[2,0,-1,0],
[3,2,-1,0],
[0,0,3,1 ],
[0,0,-1,-1],
[2,3,-2,0],
[-2,2,0,0],
[2,-2,0,-1],
[1,-1,0,-1],
[3,2,0,2]
]
