def metatree():
    input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    input = input.split(' ')
    result = []
    total = 0
    first_header = Header(2, 3, [Header, Header], [1, 1, 2])
    second_header = Header(0, 3, [],[10,11,12]) 
    third_header = Header(0, 3, [], [2])
    fourth_header = Header(0, 3, [], [99])
    result = [first_header, second_header, third_header, fourth_header]
    for i in result:
        total += sum(i.metadatas)
    return total


def header_factory():
    
    return Header() 

class Header():
    def __init__(self, childnum, metadatanum, childnodes, metadatas):
        self.childnum = childnum
        self.metadatanum = metadatanum
        self.childnodes = childnodes
        self.metadatas = metadatas


