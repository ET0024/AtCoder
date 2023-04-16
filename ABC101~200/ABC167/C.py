n, m, x = map(int, input().split())

c = []
a = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    c.append(tmp[0])
    a.append(tmp[1:])

ALL = 1 << n
ans = float('inf')
for pattern in range(ALL):
    cost = 0
    understand = [0 for _ in range(m)]

    for i in range(n):
        if pattern >> i & 1:
            cost += c[i]
            for j in range(m):
                understand[j] += a[i][j]

    # validate
    passed = True
    for j in range(m):
        if understand[j] < x:
            passed = False

    if passed and cost < ans:
        ans = cost

if ans == float('inf'):
    print(-1)
else:
    print(ans)
