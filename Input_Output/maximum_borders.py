import re

for case in range(int(input())):
    rows, cols = map(int, input().split())
    max_border = 0

    for row in range(rows):
        current_row = input()
        if '#' not in current_row:
            continue

        current_border = len(max(re.findall('#+', current_row)))

        if current_border > max_border:
            max_border = current_border

    print(max_border)
