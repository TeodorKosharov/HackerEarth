# from sys import maxsize
#
#
# def get_last_valid_index(check_index, arr_len):
#     increment = 2
#     while True:
#         if check_index + increment >= arr_len:
#             break
#         check_index += increment
#         increment += 1
#
#     return check_index
#
#
# n = int(input())
# arr = [int(x) for x in input().split()]
# max_sum = -maxsize
#
# for index in range(len(arr)):
#     current_sum = sum(arr[index: get_last_valid_index(index, n) + 1])
#     if current_sum > max_sum:
#         max_sum = current_sum
#
# print(max_sum)


# Faster approach:

size = int(input())
arr = list(map(int, input().split()))
start_index = 1
distance = 2

while start_index <= size:
    start_index += distance
    distance += 1

start_index -= distance - 1
distance -= 2
total = sum(arr[:start_index])
temp_total = total

for i in range(1, size):
    total -= arr[i - 1]

    if start_index < size:
        total += arr[start_index]
        start_index += 1

    else:
        distance -= 1
        total -= sum(arr[size - distance:size])
        start_index -= distance

    if total > temp_total:
        temp_total = total

print(temp_total)
