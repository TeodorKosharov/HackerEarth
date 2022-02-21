n = int(input())

for i in range(n):
    arr = int(input())
    el = list(map(int, input().split()))
    count = 1

    for j in range(1, arr):
        if el[j] < el[j - 1]:
            count += 1

    print(count)
