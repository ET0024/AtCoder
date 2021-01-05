a, b, x, y = map(int, input().split())

if a <= b:
    print(x + abs(a - b) * min(y, 2 * x))
else:
    print(x + abs(a - b - 1) * min(y, 2 * x))
