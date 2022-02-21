# from functools import reduce
#
# for case in range(int(input())):
#     n, k = map(int, input().split())
#     result = 0
#
#     for i in range(k):
#         formed_num = reduce(lambda x, y: x + y, [int(x) for x in str(n)])
#         result = formed_num ** 3
#         n = result
#
#     print(result)


# Recursive approach:

from functools import reduce


def digit_sum(num, turns):
    formed_num = reduce(lambda x, y: x + y, [int(x) for x in str(num)])
    result = formed_num ** 3

    if turns == 0:
        return result

    return digit_sum(result, turns - 1)


for case in range(int(input())):
    n, k = map(int, input().split())

    print(digit_sum(n, k - 1))
