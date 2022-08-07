from collections import deque

n = int(input())
sx, sy, tx, ty = map(int, input().split())

x, y, r = [], [], []
edge = [[] for _ in range(n)]
si = -1
ti = -1
for i in range(n):
    _x, _y, _r = map(int, input().split())
    x.append(_x)
    y.append(_y)
    r.append(_r)

    if (sx - _x) ** 2 + (sy - _y) ** 2 == _r ** 2:
        si = i
    if (tx - _x) ** 2 + (ty - _y) ** 2 == _r ** 2:
        ti = i

for i in range(n):
    for j in range(i + 1, n):
        d2 = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        if (r[i] - r[j]) ** 2 <= d2 <= (r[i] + r[j]) ** 2:
            edge[i].append(j)
            edge[j].append(i)

INF = 10 ** 10
reached = [False for _ in range(n)]
q = deque()
q.append(si)
reached[si] = True

while len(q) > 0:
    current = q.popleft()

    for nx in edge[current]:
        if not reached[nx]:
            reached[nx] = True
            q.append(nx)

if reached[ti]:
    print('Yes')
else:
    print('No')
