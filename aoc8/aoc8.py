import pdb
from collections import namedtuple
with open('input') as fd:
    testinput = fd.read()
testinput = iter([int(x) for x in testinput.split(' ')])
print(testinput)

def metatree(testinput):
    try:
        childnum, metadatanum = next(testinput), next(testinput)
        #print('childnum: %s %s' % (childnum, metadatanum))
        children = [metatree(testinput) for _ in range(childnum) if childnum]
        metadata = [next(testinput) for _ in range(metadatanum) if metadatanum]
    except StopIteration:
        #print('input: %s' % list(testinput))
        return
    if children:
        return children, sum(metadata)
    else:
        return sum(metadata)
t=0
def total(res):
    global t
    for x in res:
        try:
            total(x)
        except TypeError:
            print(x)
            t+=x
    return t

result = metatree(testinput)
print(total(result))
