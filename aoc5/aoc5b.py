import pdb
import string

def reader():
    with open('input') as fd:
        data = fd.read().strip()
    return data

def parser(data):
    while True:
        if not data:
            return ''
        if len(data) ==1:
            return data
        if len(data) ==2:
            if data[0] == data[1].swapcase():
               return ''
            else:
                return data
        for i, letter in enumerate(data[:-1]):
            if letter == data[i+1].swapcase():
                data=data[:i] + data[i+2:]
                break
        else:
            return data

def transform(letter, data):
    data = data.replace(letter, '')
    data = data.replace(letter.swapcase(), '')
    return parser(data)


def main():
    data = reader()
    res = []
    for letter in string.ascii_lowercase:
        print('checking {}'.format(letter))
        amount = len(transform(letter, data))
        res.append(amount)
        print('result {} {}'.format(letter, amount))

    print('result {}'.format(min(res)))


if __name__ == '__main__':
    main()




            

