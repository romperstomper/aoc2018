from datetime import datetime
import re

def readinput():
    with open('input') as fd:
        data = fd.read().splitlines()
    data.sort(key=lambda x: datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'))
    return data


def count():
    "[1518-05-18 00:01] Guard #1171 begins shift"
    lines = readinput()
    re.search(r'Guard #(\d+)', lines[0])

print(count())
