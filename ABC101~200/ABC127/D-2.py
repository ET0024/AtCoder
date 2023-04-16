from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
d = defaultdict(int)
for _ in range(m):
    b, c = map(int, input().split())
    d[c] += b

d2 = sorted(list(d.items()), reverse=True)

rep = []
for k, v in d2:
    while 0 < v and len(rep) < n:
        rep.append(k)
        v -= 1

while len(rep) < n:
    rep.append(0)

ans = 0
for i in range(n):
    ans += max(a[i], rep[i])

print(ans)