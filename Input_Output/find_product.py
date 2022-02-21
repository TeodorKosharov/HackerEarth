n = int(input())
arr = [int(x) for x in input().split()]

answer = 1
for i in arr:
    answer = (answer * i) % (10 ** 9 + 7)

print(answer)
