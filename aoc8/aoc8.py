"""Module strings"""

def myread():
    """Module strings"""
    with open('input') as f_d:
        _testinput = f_d.read()
        testinput = iter([int(x) for x in _testinput.split(' ')])
    return testinput



class Aoc8():
    """class strings"""
    def __init__(self):
        """
        strings mcdocstrings
        """
        self.tot = 0

    def metatree(self, testinput):
        """
        strings mcdocstrings
        """
        try:
            childnum, metadatanum = next(testinput), next(testinput)
            children = [self.metatree(testinput) for _ in range(childnum) if childnum]
            metadata = [next(testinput) for _ in range(metadatanum) if metadatanum]
        except StopIteration:
            return None
        if children:
            return children, sum(metadata)
        return sum(metadata)

    def total(self, res):
        """
        moar strings mcdocstrings
        """
        for elem in res:
            try:
                self.total(elem)
            except TypeError:
                self.tot += elem
        return self.tot
