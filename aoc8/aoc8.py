def metatree():
    input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    input = input.split(' ')
    return input


class Header():
    def __init__(childnum, metadatanum, childnodes, metadatas):
        self.childnum = childnum
        self.metadatanum = metadatanum
        self.childnodes = childnodes
        self.metadatas = metadatas


