N = int(input())
a = []
b = []
c = []
for _ in range(N):
    _a, _b, _c = map(int, input().split())
    a.append(_a)
    b.append(_b)
    c.append(_c)

dpa = [0] * N
dpb = [0] * N
dpc = [0] * N
dpa[0] = a[0]
dpb[0] = b[0]
dpc[0] = c[0]

for i in range(1, N):
    dpa[i] = a[i] + max(dpb[i - 1], dpc[i - 1])
    dpb[i] = b[i] + max(dpa[i - 1], dpc[i - 1])
    dpc[i] = c[i] + max(dpa[i - 1], dpb[i - 1])

print(max(dpa[-1], dpb[-1], dpc[-1]))