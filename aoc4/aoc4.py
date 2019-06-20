from datetime import datetime
from collections import defaultdict
import re
import pdb
import operator

def readinput():
    with open('input') as fd:
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
            if date not in guards[guard]:
                guards[guard][date] = {k:0 for k in range(60)}
        if 'wakes' in line:
            for i in range(falls, time.minute):
                guards[guard][date][i]=+1 
    return guards

def totalminutes():
    # pdb.set_trace()
    theroster = roster()
    result = {}
    subresult = 0
    for guard in theroster:
        for i in theroster[guard]:
            subresult += sum(theroster[guard][i][y] for y in theroster[guard][i])
            result[guard]= subresult
        subresult = 0
    return result

def sleepiestguard():
    result = totalminutes()
    return max(result.items(), key=operator.itemgetter(1))[0]

def mostminutes():
    sleepy = sleepiestguard()
    theroster = roster()
    k, v = theroster[sleepy].popitem()
    total = {k:v}
    for date in theroster[sleepy]:
        #pdb.set_trace()
        for i in theroster[sleepy][date]:
            total[k][i] += theroster[sleepy][date][i]
    return max(total[k].items(), key=operator.itemgetter(1))[0]*sleepy


print(mostminutes())

