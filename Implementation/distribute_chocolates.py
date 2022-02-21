for x in range(int(input())):
    c, n = map(int, input().split())
    a = n * (n - 1) // 2
    b = (c - a) // n

    if b < 1:
        print(c)
    else:
        left = c - (b * n + a)
        print(left)
