from datetime import datetime
from collections import defaultdict
import re
import pdb

def readinput():
    with open('small') as fd:
        data = fd.read().splitlines()
    return data

def sort_data():
    '[1518-11-01 00:00] Guard #10 begins shift'
    data = [(datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'), x[18:]) for x in readinput()]
    data.sort()    
    return data

def roster():
    data = sort_data()
    guards = defaultdict(dict)
    for time, line in data:
        match = re.search('Guard #(\d+)', line)
        guard = int(match.group(1)) if match else guard
        if 'falls' in line:
            date = str(time.strftime('%Y-%m-%d'))
            falls = time.minute
            guards[guard][date] = {k:0 for k in range(60)}
        if 'wakes' in line:
            for i in range(falls, time.minute):
                guards[guard][date][i]=+1 
    return guards

def totalminutes():
    shift10 = roster()[10]
    # pdb.set_trace()
    result = 0
    for i in shift10:
        print(i)
        result += sum(shift10[i][y] for y in shift10[i])
        print(result)
    print(result)


totalminutes()

