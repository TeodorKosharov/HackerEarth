# def are_elements_equal(arr):
#     for i in range(len(arr) - 1):
#         if arr[i] != arr[i + 1]:
#             return False
#     return True
#
#
# n = int(input())
# arr1 = [int(x) for x in input().split()]
# arr2 = [int(x) for x in input().split()]
#
# steps = 0
#
# while not are_elements_equal(arr1):
#     is_arr_changed = False
#     min_value = min(arr1)
#
#     for index in range(len(arr1)):
#         if arr1[index] == min_value:
#             continue
#
#         if arr1[index] >= arr2[index]:
#             arr1[index] -= arr2[index]
#             steps += 1
#             is_arr_changed = True
#
#     if not is_arr_changed:
#         print(-1)
#         exit(0)
#
# print(steps)


# Faster approach:

n = int(input())

first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))
min_val = min(first_array)
count = 0

i = 0

while i < n:
    while first_array[i] > min_val:
        first_array[i] -= second_array[i]
        count += 1

    if first_array[i] < min_val:
        min_val = first_array[i]
        i = 0

    elif first_array[i] < 0:
        count = -1
        break
    else:
        i += 1

print(count)
