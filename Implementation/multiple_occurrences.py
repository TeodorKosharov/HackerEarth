for case in range(int(input())):
    n = int(input())
    integers = input().split()
    result = 0
    values = {}

    for index in range(len(integers)):
        if integers[index] not in values:
            values[integers[index]] = [index, 0]
        else:
            values[integers[index]][1] = index

    for number, data in values.items():
        if data[1] != 0:
            result += (data[1] + 1) - (data[0] + 1)

    print(result)
