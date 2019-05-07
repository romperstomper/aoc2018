from collections import Counter
import pprint

def readinput():
    with open('input') as fd:
        data = fd.read().splitlines()
    return data

def cords():
    allcords = readinput()
    data =[]
    for cord in allcords:
        _, _, s, w = cord.split(' ')
        s = s.rstrip(':')
        x = [int(x) for x in s.split(',')]
        y = [int(x) for x in w.split('x')]
        data.append((tuple(x), tuple(y)))
    
    return data

def gen_cords():
    res = []
    for line in cords():
        (x,y),(i,j)=line
        res.append([(a, k) for a in range(x, x+i) for k in range(y, y+j)])
    return [val for sublist in res for val in sublist]

def ddict():
    c = Counter(gen_cords())
    res=(Counter(el for el in c.elements() if c[el] > 1))

def leftover():
    c = Counter(gen_cords())
    res=(Counter(el for el in c.elements() if c[el] ==1))
    for n, line in enumerate(cords()):
        print('number is: %s' % (n+1))
        (x,y),(i,j)=line
        coords = [(a, k) for a in range(x, x+i) for k in range(y, y+j)]
        if set(coords).issubset(res):
            print('\n')
            print(line)
            print('\n')
            break

