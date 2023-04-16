from collections import defaultdict

h, w, n = map(int, input().split())
a = []
b = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

# 座標圧縮
table_a = defaultdict()
for i, val in enumerate(sorted(list(set(a)))):
    table_a[val] = i + 1

table_b = defaultdict()
for i, val in enumerate(sorted(list(set(b)))):
    table_b[val] = i + 1

for i in range(n):
    print(table_a[a[i]], table_b[b[i]])
