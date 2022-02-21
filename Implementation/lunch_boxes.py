for case in range(int(input())):
    boxes, schools = map(int, input().split())
    integers = [int(x) for x in input().split()]

    delivered_boxes = 0
    for i in sorted(integers):
        if boxes == 0:
            break
        if boxes >= i:
            boxes -= i
            delivered_boxes += 1

    print(delivered_boxes)
