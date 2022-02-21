for case in range(int(input())):
    word = input()
    print(''.join(sorted(word)) if word != word[::-1] else -1)
