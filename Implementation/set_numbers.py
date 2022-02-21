for case in range(int(input())):
    num = int(input())

    for i in range(num, 0, -1):
        value = bin(i)
        if len(value) - 2 == value.count('1'):
            print(i)
            break
