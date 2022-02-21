num = int(input())

for each in range(num):
    x, k = map(int, input().split())
    flag = True

    while x > 0:
        if x % k >= 2:
            print("NO")
            flag = False
            break
        else:
            x //= k
    if flag:
        print("YES")
