def read_input():
    result = []
    with open('input') as fd:
        data = fd.readlines()
    result.append(data[0].split('<')[1])
    print(result)

read_input()

