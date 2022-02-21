x, y, k = map(int, input().split())
print(len([num for num in range(x, y + 1) if num % k == 0]))
