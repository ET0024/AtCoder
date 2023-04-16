from collections import defaultdict
import heapq

n, m = map(int, input().split())
edge = [[] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c, i))  # to_node, cost, index
    edge[b].append((a, c, i))  # to_node, cost, index

used = defaultdict(bool)
visited = [False for _ in range(n)]
q = []

visited[0] = True
for nx, c, i in edge[0]:
    heapq.heappush(q, (c, nx, i))
connected = 1

while len(q) > 0:
    c, nx, i = heapq.heappop(q)
    if visited[nx]:
        continue
    used[i] = True
    visited[nx] = True
    connected += 1
    if connected == n:
        break
    for nx2, c2, i2 in edge[nx]:
        if not visited[nx2]:
            heapq.heappush(q, (c2, nx2, i2))

ans = 0
for i in range(n):
    for nx, c, ind in edge[i]:
        if not used[ind] and c > 0:
            ans += c

print(ans // 2)
