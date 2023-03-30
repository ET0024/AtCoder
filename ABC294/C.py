from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = defaultdict(int)

c = sorted(a+b)
for i, val in enumerate(c):
    d[val] = i + 1

print(*[d[a[i]] for i in range(n)])
print(*[d[b[i]] for i in range(m)])