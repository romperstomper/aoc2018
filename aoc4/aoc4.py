from datetime import datetime
import re


def readinput():
    with open('small') as fd:
        data = fd.read().splitlines()
    return data


def sort_data():
    '[1518-11-01 00:00] Guard #10 begins shift'
    data = [(datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'), x[18:]) for x in readinput()]
    data.sort()    
    return data




