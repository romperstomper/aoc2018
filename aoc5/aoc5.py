import pdb

def reader():
    #return 'dabAcCaCBAcCcaDA'
    return 'abBA'

def parser(data):
    while True:
        if not data:
            return ''
        if len(data) ==1:
            return data
        if len(data) ==2:
            if data[0] == data[1].swapcase():
               return ''
            else:
                return data
        for i, letter in enumerate(data[:-1]):
            if letter == data[i+1].swapcase():
                data=data[:i] + data[i+2:]
                break
        else:
            return data
        
from string import *


def collapse(s):
    p = ['.']
    for u in s:
        v = p[-1]
        if v != u and v.lower() == u.lower():
            p.pop()
        else:
            p.append(u)
    return len(p) - 1


def main():
    with open('input') as fd:
        data = fd.read().strip()
    result = parser(data)
    with open('out', 'w+') as wd:
        wd.write(result)

if __name__ == '__main__':
    main()




            

