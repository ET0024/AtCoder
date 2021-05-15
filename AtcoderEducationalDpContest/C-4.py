n = int(input())
a = []
b = []
c = []
for _ in range(n):
    _a, _b, _c = map(int, input().split())
    a.append(_a)
    b.append(_b)
    c.append(_c)

dp_a = [0 for _ in range(n)]
dp_b = [0 for _ in range(n)]
dp_c = [0 for _ in range(n)]

dp_a[0] = a[0]
dp_b[0] = b[0]
dp_c[0] = c[0]

for i in range(1, n):
    dp_a[i] = a[i] + max(dp_b[i - 1], dp_c[i - 1])
    dp_b[i] = b[i] + max(dp_c[i - 1], dp_a[i - 1])
    dp_c[i] = c[i] + max(dp_a[i - 1], dp_b[i - 1])

print(max(dp_a[-1], dp_b[-1], dp_c[-1]))
