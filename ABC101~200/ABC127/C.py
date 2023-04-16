n, m = map(int, input().split())

l2 = -1
r2 = n + 1
for _ in range(m):
    l, r = map(int, input().split())
    l2 = max(l2, l)
    r2 = min(r2, r)

if l2 <= r2:
    print(r2 - l2 + 1)
else:
    print(0)
