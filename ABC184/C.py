def reachable(x1, y1, x2, y2):
    if x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2 or abs(x1 - x2) + abs(y1 - y2) <= 3:
        return True


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if x1 == x2 and y1 == y2:
    print(0)
    exit()

if reachable(x1, y1, x2, y2):
    print(1)
    exit()

for i in range(-2, 2 + 1):
    for j in range(-2, 2 + 1):
        if reachable(x1 + i, y1 + j, x2, y2):
            print(2)
            exit()

    if reachable(x1 + 3, y1, x2, y2) or \
            reachable(x1 - 3, y1, x2, y2) or \
            reachable(x1, y1 + 3, x2, y2) or \
            reachable(x1, y1 - 3, x2, y2):
        print(2)
        exit()

    if (x1 + y1 - x2 - y2) % 2 == 0:
        print(2)
        exit()

print(3)
