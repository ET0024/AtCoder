from collections import deque
from collections import defaultdict

n, x, y = map(int, input().split())
x -= 1
y -= 1
edge = [[] for _ in range(n)]
for i in range(n - 1):
    edge[i].append(i + 1)
    edge[i + 1].append(i)
edge[x].append(y)
edge[y].append(x)

# 全探索
count = defaultdict(int)
for start in range(n):
    dist = [-1 for _ in range(n)]
    q = deque()
    dist[start] = 0
    q.append(start)

    while len(q) > 0:
        current = q.popleft()
        for nx in edge[current]:
            if dist[nx] < 0:
                dist[nx] = dist[current] + 1
                q.append(nx)

    for d in dist:
        count[d] += 1

for k in range(1, n):
    print(count[k] // 2)
