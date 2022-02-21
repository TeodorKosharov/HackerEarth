# Detailed solution:

# n = int(input())
# arr = [x for x in input().split()]
#
# formed_number = ''
#
# for num in arr:
#     formed_number += num[-1]
#
# if int(formed_number) % 10 == 0:
#     print('Yes')
# else:
#     print('No')


# Short solution:

n = int(input())
arr = [x for x in input().split()]
print('Yes' if int("".join(x[-1] for x in arr)) % 10 == 0 else 'No')

# First I'm making a list containing only the last chars of every element in the array.
# Next I'm concatenating them in a whole string using the join method
# Finally I transformed that string to an integer then checked if it is divisable by 10 without reminder
