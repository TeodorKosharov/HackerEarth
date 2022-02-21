# from functools import reduce
#
# n = int(input())
# supernatural_numbers = 0
#
# for i in range(0, 1_000_000):
#     i = str(i)
#     if '1' not in i:
#         if n == reduce(lambda x, y: x * y, [int(x) for x in i]):
#             supernatural_numbers += 1
#
# print(supernatural_numbers)


# Shorter approach:

from functools import reduce

n = int(input())
supernatural_numbers = 0

for i in range(0, 1_000_000):
    i = str(i)
    supernatural_numbers += 1 if '1' not in i and n == reduce(lambda x, y: x * y, [int(x) for x in i]) else 0

print(supernatural_numbers)
