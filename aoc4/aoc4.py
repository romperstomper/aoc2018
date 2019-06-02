from datetime import datetime
import re
import pdb
from collections import defaultdict

def readinput():
    with open('input') as fd:
        data = fd.read().splitlines()
    data.sort(key=lambda x: datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'))
    return data


def create_guards():
    guards = {}
    lines = readinput()
    for line in lines:
        match = re.search(r'Guard #(\d+)', line)
        if match:
            if match.group(1) in guards:
                continue
            else:
                guards[match.group(1)] = {k:0 for k in range(60)}
    return guards

#print(count())
print(create_guards().keys())
