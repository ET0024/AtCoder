import math

n, k = map(int, input().split())
a = list(map(int, input().split()))
x = []
y = []
for _ in range(n):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)

b = list(set([i + 1 for i in range(n)]) - set(a))

ans = 0
for person in b:
    person -= 1
    tmp = 10 ** 20
    for light in a:
        light -= 1
        tmp = min((x[person] - x[light]) ** 2 + (y[person] - y[light]) ** 2, tmp)
    ans = max(ans, tmp)

print(math.sqrt(ans))
