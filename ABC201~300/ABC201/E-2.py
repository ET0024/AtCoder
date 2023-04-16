from collections import deque

N = int(input())
edge = [[] for _ in range(N)]
deg = [0 for _ in range(N)]
dist = [-1 for _ in range(N)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append((v, w))
    edge[v].append((u, w))
    deg[u] += 1
    deg[v] += 1

for i in range(N - 1):
    if deg[i] == 1:
        start = i

q = deque()
dist[start] = 0
q.append(start)

while len(q) > 0:
   node = q.popleft()
   for nx, w in edge[node]:
       if dist[nx]<0:
           dist[nx] = dist[node] ^ w
           q.append(nx)

print(dist)