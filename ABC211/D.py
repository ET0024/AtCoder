import heapq

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

visited = [False for _ in range(n)]
dist = [float('inf') for _ in range(n)]
count = [0 for _ in range(n)]
q = []

dist[0] = 0
count[0] = 1
q.append((0, 0))

while len(q) > 0:
    cost, current = heapq.heappop(q)
    if visited[current]:
        continue
    visited[current] = True

    for nx in edge[current]:
        if visited[nx]:
            continue
        if dist[nx] > cost + 1:
            dist[nx] = cost + 1
            heapq.heappush(q, (cost + 1, nx))
            count[nx] = count[current]
        elif dist[nx] == cost + 1:
            count[nx] += count[current]

print(count[-1] % (10 ** 9 + 7))
