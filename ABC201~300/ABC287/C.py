from collections import deque

n, m = map(int, input().split())

edge = [[] for _ in range(n)]
degree = [0] * n
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    degree[u] += 1
    degree[v] += 1
    edge[u].append(v)
    edge[v].append(u)

# judge if graph is connected
q = deque()
reached = [False for _ in range(n)]
q.append(0)

while len(q) > 0:
    node = q.popleft()
    if not reached[node]:
        reached[node] = True
    for nx in edge[node]:
        if reached[nx]:
            continue
        q.append(nx)

if reached.count(True) != n:
    print('No')
    exit()

if degree.count(1) == 2 and degree.count(2) == n - 2:
    print('Yes')
else:
    print('No')
