# Detailed solution:

# n = int(input())
# arr = input().split()
#
# left_half = arr[:len(arr) // 2]
# right_half = arr[len(arr) // 2:]
#
# left_half_number = ''
# right_half_number = ''
#
# for element in left_half:
#     left_half_number += element[0]
#
# for element in right_half:
#     right_half_number += element[-1]
#
# generated_number = int(left_half_number + right_half_number)
#
# print('OUI' if generated_number % 11 == 0 else 'NON')


# Short solution:

n = int(input())
arr = input().split()
print('OUI' if int(''.join(x[0] for x in arr[:len(arr) // 2]) + ''.join(x[-1] for x in arr[len(arr) // 2:])) % 11 == 0 else 'NON')
