for case in range(int(input())):
    x, y = [int(x) for x in input().split()]
    print(x if x >= y >= 0 else -1)
