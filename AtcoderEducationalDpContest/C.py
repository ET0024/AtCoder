N = int(input())
a = []
b = []
c = []
for _ in range(N):
    _a, _b, _c = map(int, input().split())
    a.append(_a)
    b.append(_b)
    c.append(_c)

dp_a = [0] * N
dp_b = [0] * N
dp_c = [0] * N

dp_a[0] = a[0]
dp_b[0] = b[0]
dp_c[0] = c[0]

for i in range(1, N):
    dp_a[i] = max(dp_b[i - 1], dp_c[i - 1]) + a[i]
    dp_b[i] = max(dp_a[i - 1], dp_c[i - 1]) + b[i]
    dp_c[i] = max(dp_a[i - 1], dp_b[i - 1]) + c[i]

print(max(dp_a[-1], dp_b[-1], dp_c[-1]))
