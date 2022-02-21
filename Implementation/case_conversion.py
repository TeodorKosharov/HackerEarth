for case in range(int(input())):
    word = input()
    result = ''

    for index in range(len(word) - 1):
        if word[index + 1].isupper():
            result += word[index].lower() + '_'
        else:
            result += word[index].lower()
    result += word[-1].lower()
    print(result)
