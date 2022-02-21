import re

ticket = input()
vowels = ["A", "E", "I", "O", "U", "Y"]

if re.findall('[A-Z]', ticket)[0] in vowels:
    print('invalid')
    exit(0)

for index in range(len(ticket) - 1):
    if ticket[index].isdigit() and ticket[index + 1].isdigit():
        if (int(ticket[index]) + int(ticket[index + 1])) % 2 != 0:
            print('invalid')
            exit(0)

print('valid')
