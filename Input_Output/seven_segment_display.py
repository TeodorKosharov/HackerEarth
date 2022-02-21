def get_all_matchsticks(number):
    return sum([numbers_matchsticks[int(x)] for x in number])


def maximize_number(remaining_sticks, formed_num):
    number = list(formed_num)

    for index in range(len(number)):
        remaining_sticks += numbers_matchsticks[int(number[index])]

        for value, sticks in sorted(numbers_matchsticks.items(), key=lambda x: -x[0]):
            if remaining_sticks >= sticks:
                number[index] = value
                remaining_sticks -= sticks

            if remaining_sticks < 2:
                break

    return ''.join(str(x) for x in number)


numbers_matchsticks = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}
numbers_matchsticks = dict(sorted(numbers_matchsticks.items(), key=lambda x: (x[1], -x[0])))

for case in range(int(input())):
    n = input()
    available_matchsticks = get_all_matchsticks(n)

    formed_number = ''
    nums = tuple(numbers_matchsticks.keys())
    current_num_index = 0

    while current_num_index < len(nums) and available_matchsticks >= 2:
        if numbers_matchsticks[nums[current_num_index]] <= available_matchsticks:
            available_matchsticks -= numbers_matchsticks[nums[current_num_index]]
            formed_number += str(nums[current_num_index])
        else:
            current_num_index += 1

    print(maximize_number(available_matchsticks, formed_number))
