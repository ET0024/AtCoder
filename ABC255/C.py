x, a, d, n = map(int, input().split())

y = x - a

if d == 0:
    print(abs(y))
    exit()

if y < min(0, (n - 1) * d):
    print(abs(y - min(0, (n - 1) * d)))
elif y > max(0, (n - 1) * d):
    print(abs(y - max(0, (n - 1) * d)))
else:
    print(min(abs(y % d), abs(y % d - d)))
