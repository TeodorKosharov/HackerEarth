for case in range(int(input())):
    number = int(input())
    result = 0

    for i in range(1, number + 1):
        result += number // i

    print(result)
