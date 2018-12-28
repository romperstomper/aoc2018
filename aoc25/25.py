from collections import namedtuple

def readinput():
    cords = namedtuple("Cords", ['w', 'x', 'y', 'z'])

    result = set()
    with open('input') as fd:
        data = fd.read().splitlines()
    for line in data:
        result.add(cords(*line.split(',')))
    return result

print(readinput())


