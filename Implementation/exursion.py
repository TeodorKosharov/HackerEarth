from math import ceil

for case in range(int(input())):
    boys, girls, seats = map(int, input().split())
    print(ceil(boys / seats) + ceil(girls / seats))
