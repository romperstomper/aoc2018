import re
def read():
    with open('input') as fd:
        data = fd.read().splitlines()
    return data

def count(data):
    result = []
    target =  ' '.join(data)
    for w in data:
        for n,_ in enumerate(w):
            pat = w[:n] + '.' + w[n+1:]
            matches = re.findall(pat, target)
            if len(matches) > 1:
                result.append(matches)
    s1 = result[0][0]
    s2 = result[0][1]
    print(''.join(set(s1)&set(s2)))

count(read())

            
