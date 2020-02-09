class Header():
    def __init__(self, childnum, metadatanum, childnodes, metadatas):
        self.childnum = childnum
        self.metadatanum = metadatanum
        self.childnodes = childnodes
        self.metadatas = metadatas

first_header = Header(2, 3, [Header, Header], [1, 1, 2])
second_header = Header(0, 3, [],[10,11,12]) 
third_header = Header(0, 3, [], [2])
fourth_header = Header(0, 3, [], [99])
input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')

def metatree(input):
    input = map(int, iter(input))
    childnum, metadatanum = next(input), next(input)
    children = [metatree(input) for _ in range(childnum)]
    metadatas = [next(input) for _ in range(metadatanum)]
    return (children, metadatas)
    
total = 0
print(metatree(input))
#while True:
#    try:
#        print(metatree(input))
#    except StopIteration:
#        break
