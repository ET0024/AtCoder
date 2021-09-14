import bisect

h, w, n = map(int, input().split())
a = []
b = []

row = set()
col = set()
for _ in range(n):
    _a, _b = map(int, input().split())
    _a -= 1
    _b -= 1
    a.append(_a)
    b.append(_b)
    row.add(_a)
    col.add(_b)

row = sorted(list(row))
col = sorted(list(col))

for i in range(n):
    a2 = bisect.bisect_right(row, a[i] - 1)
    b2 = bisect.bisect_right(col, b[i] - 1)
    print(a2 + 1, b2 + 1)