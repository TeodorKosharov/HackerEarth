grids = int(input())
pattern = input()
length = len(pattern) - 1

if pattern.find("HH") != -1:
    print("NO")
else:
    pattern = pattern.replace('.', 'B')
    print("YES")
    print(pattern)
