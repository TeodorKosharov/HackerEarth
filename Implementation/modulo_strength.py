# n, k = map(int, input().split())
# arr = [int(x) for x in input().split()]
#
# strength = 0
# elements = len(arr)
# remainder = 0
#
# while elements:
#     res = [x for x in arr if x % k == remainder]
#     elements -= len(res)
#     strength += (len(res) - 1) * len(res)
#     remainder += 1
#
# print(strength)

# Faster approach:

n, k = map(int, input().split())
arr = [int(x) for x in input().split()]

remainders = {}
strength = 0

for num in arr:
    current_remainder = num % k
    if current_remainder not in remainders:
        remainders[current_remainder] = 0

    remainders[current_remainder] += 1

for reminder_count in remainders.values():
    strength += (reminder_count - 1) * reminder_count

print(strength)
