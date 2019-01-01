from collections import namedtuple
import itertools
DATA = [
[0,0,0,0],
[3,0,0,0],
[0,3,0,0],
[0,0,3,0],
[0,0,0,3],
[0,0,0,6],
[9,0,0,0],
[12,0,0,0]
]
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
import pdb
def readfileinput():
    cords = namedtuple("Cords", ['w', 'x', 'y', 'z'])

    result = list()
    with open('input') as fd:
        data = fd.read().splitlines()
    for line in data:
        result.append(list(map(int, cords(*line.split(',')))))
    return result

def checkrange(a, b):
    w,x,y,z = a
    w2,x2,y2,z2 = b
    print('score: ', (w - w2)+(x - x2)+(y - y2)+(z - z2))
    if -3 <= (w - w2)+(x - x2)+(y - y2)+(z - z2) <= 3:
        return True
    return False

def countconstellations(cords):
    result = []
    tmp = set()
    for i, cord in enumerate(cords[:-1]):
        print(cord, cords[i+1])
        print('result', checkrange(cord, cords[i+1]))
        if checkrange(cord, cords[i+1]):
            tmp.add(cords[i+1])
        else:
            print('sfdk', cord, cords[i+1])
            result.append(tmp)
            tmp = set()
    return result

        
def formatter(data):
    result = list()
    for line in data:
        w,x,y,z = line
        result.append((w,x,y,z))
    return result

result = countconstellations(((0,0,0,6), (9,0,0,0)))
print(result)
