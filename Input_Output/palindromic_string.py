# word = input()
#
# for index in range(len(word) // 2):
#     if word[index] != word[-1 - index]:
#         print('NO')
#         exit(0)
#
# print('YES')

# Short solution:

word = input()
print('YES' if word == word[::-1] else 'NO')
