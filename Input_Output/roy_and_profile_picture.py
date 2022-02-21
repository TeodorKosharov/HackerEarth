l = int(input())

for photo in range(int(input())):
    w, h = map(int, input().split())

    if w < l or h < l:
        print('UPLOAD ANOTHER')
    elif w == h:
        print('ACCEPTED')
    else:
        print('CROP IT')
