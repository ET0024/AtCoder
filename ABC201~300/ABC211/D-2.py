from collections import deque

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

MOD = 10 ** 9 + 7
dist = [float('inf') for _ in range(n)]
route = [0 for _ in range(n)]

dist[0] = 0
route[0] = 1
q = deque()
q.append(0)
while len(q) > 0:
    current = q.popleft()

    for nx in edge[current]:
        d = dist[current] + 1
        if d < dist[nx]:
            dist[nx] = d
            route[nx] = route[current]
            route[nx] %= MOD
            q.append(nx)
        elif d == dist[nx]:
            route[nx] += route[current]
            route[nx] %= MOD

print(route[-1])
