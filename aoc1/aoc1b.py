import operator
import pdb

def readinput():
    with open('input') as fd:
        data = [line.strip() for line in fd]
    return data

def main():
    data = readinput()
    result = 0
    resultset = {result}
    ops = { "+": operator.add, "-": operator.sub }
    while True:
        for line in data:
            result = ops[line[0]](result, int(line[1:]))
            if result in resultset:
                print("result {}".format(result))
                return 
            resultset.add(result)

if __name__ == '__main__':
    main()
