for case in range(int(input())):
    number = int(input())
    for current_number in range(number, number + 10):
        if sum([int(x) for x in str(current_number)]) % 4 == 0:
            print(current_number)
            break
