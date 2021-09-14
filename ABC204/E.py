import heapq
import math

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))

q = []
q.append((0, 0))  # dist, node
dist = [float('inf') for _ in range(n)]
dist[0] = 0
visited = [False for _ in range(n)]

while len(q) > 0:

    cost, node = heapq.heappop(q)
    if visited[node]:
        continue
    visited[node] = True

    for nxt, c, d in graph[node]:
        if not visited[nxt]:
            th = int(math.sqrt(d)) - 1

            if th >= cost:
                cost_nxt = cost + c + math.floor(d / (cost + 1))
                cost_nxt2 = th + c + math.floor(d / (th + 1))
                cost_nxt3 = th + 1 + c + math.floor(d / (th + 2))
                cost_nxt = min(cost_nxt, cost_nxt2, cost_nxt3)
            elif th + 1 >= cost:
                cost_nxt = cost + c + math.floor(d / (cost + 1))
                cost_nxt3 = th + 1 + c + math.floor(d / (th + 2))
                cost_nxt = min(cost_nxt, cost_nxt3)
            else:
                cost_nxt = cost + c + math.floor(d / (cost + 1))

            if dist[nxt] > cost_nxt:
                dist[nxt] = cost_nxt
                heapq.heappush(q, (dist[nxt], nxt))

if not visited[-1]:
    print(-1)
else:
    print(dist[-1])
