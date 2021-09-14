# 路線の表現が必要...

import heapq

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
corp = []
for i in range(m):
    p, q, c = map(int, input().split())
    p -= 1
    q -= 1
    edge[p].append(q)
    edge[q].append(p)
    corp.append(c)

dist = [float('inf') for _ in range(n)]
visited = [False for _ in range(n)]

dist[0] = 1
q = [(1, 0)]

while len(q) > 0:
    cost, current = heapq.heappop(q)

    if visited[current]:
        continue

    visited[current] = True

    for nx in edge[current]:
        if corp[nx] == corp[current]:
            if not visited[nx] and cost < dist[nx]:
                dist[nx] = cost
                heapq.heappush(q, (cost, nx))
        else:
            if not visited[nx] and cost + 1 < dist[nx]:
                dist[nx] = cost + 1
                heapq.heappush(q, (cost + 1, nx))

if dist[-1] == float('inf'):
    print(-1)
else:
    print(dist[-1])
