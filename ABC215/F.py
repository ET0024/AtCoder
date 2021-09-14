import bisect

n = int(input())

z = []
for _ in range(n):
    _x, _y = map(int, input().split())
    z.append((_x, _y))

z.sort()

x = []
y = []
for _z in z:
    x.append(_z[0])
    y.append(_z[1])

ans = 0
for i in range(1, n):
    d = min(abs(x[0] - x[i]), abs(y[0] - y[i]))
    if d > ans:
        ans = d

for i in range(1, n):
    # 二分探索
    left = bisect.bisect_left(x, x[i] - d)
    right = bisect.bisect_right(x, x[i] + d)

    for j in range(left + 1):
        d = min(abs(x[i] - x[j]), abs(y[i] - y[j]))
        if d > ans:
            ans = d

    for j in range(right, n):
        d = min(abs(x[i] - x[j]), abs(y[i] - y[j]))
        if d > ans:
            ans = d

print(ans)
