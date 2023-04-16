n, m = map(int, input().split())
a = []
b = []
c = []
d = []

for _ in range(m):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)

k = int(input())

for _ in range(k):
    _c, _d = map(int, input().split())
    c.append(_c)
    d.append(_d)

ALL = 1 << k
ans = 0
for pattern in range(ALL):
    count = [0 for _ in range(n + 1)]

    # placing balls simulation
    for j in range(k):
        # j人目
        if pattern >> j & 1 == 1:
            count[c[j]] += 1
        else:
            count[d[j]] += 1

    # condition judge
    satisfied = 0
    for i in range(m):
        if count[a[i]] > 0 and count[b[i]] > 0:
            satisfied += 1

    if satisfied > ans:
        ans = satisfied

print(ans)
