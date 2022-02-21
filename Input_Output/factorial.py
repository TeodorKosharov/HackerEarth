from functools import reduce

print(reduce(lambda a, b: a * b, [x for x in range(1, int(input()) + 1)]))
