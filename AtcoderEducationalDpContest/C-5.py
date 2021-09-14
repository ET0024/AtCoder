n = int(input())
a = []
b = []
c = []
for _ in range(n):
    _a, _b, _c = map(int, input().split())
    a.append(_a)
    b.append(_b)
    c.append(_c)

dpa = [0 for _ in range(n)]
dpb = [0 for _ in range(n)]
dpc = [0 for _ in range(n)]

dpa[0] = a[0]
dpb[0] = b[0]
dpc[0] = c[0]

for i in range(1, n):
    dpa[i] = max(dpb[i - 1] + a[i], dpc[i - 1] + a[i])
    dpb[i] = max(dpc[i - 1] + b[i], dpa[i - 1] + b[i])
    dpc[i] = max(dpa[i - 1] + c[i], dpb[i - 1] + c[i])

print(max(dpa[-1], dpb[-1], dpc[-1]))
