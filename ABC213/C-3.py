from collections import defaultdict

h, w, n = map(int, input().split())
a = []
b = []
for _ in range(n):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)

table_a = defaultdict(int)
table_b = defaultdict(int)

for i, val in enumerate(sorted(list(set(a)))):
    table_a[val] = i + 1

for i, val in enumerate(sorted(list(set(b)))):
    table_b[val] = i + 1

for i in range(n):
    print(table_a[a[i]], table_b[b[i]])
