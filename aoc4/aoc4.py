from datetime import datetime

def order():
    lines = [
        "[1518-11-22 00:49] wakes up",
        "[1518-05-18 00:01] Guard #1171 begins shift",
        "[1518-11-20 00:28] wakes up",
        "[1518-10-27 00:37] wakes up"
    ]
    dates = [datetime.strptime(x[1:17], '%Y-%m-%d %H:%M') for x in lines]

    return sorted(dates)

