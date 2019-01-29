import operator

def readinput():
    with open('input') as fd:
        data = fd.readlines()
    return data

def calc():
    result = 0
    ops = { "+": operator.add, "-": operator.sub }
    data = readinput()
    for line in data:
        result = ops[line[0]](result, int(line[1:]))
    return result

print("calc: {}".format(calc()))



