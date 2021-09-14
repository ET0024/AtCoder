import heapq

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c, i))
    edge[b].append((a, c, i))

q = []
visited = [False for _ in range(n)]
used = [False for _ in range(m)]
visited[0] = True
connect = 1
for nx, cost, i in edge[0]:
    heapq.heappush(q, (cost, nx, i))

while connect < n and len(q) > 0:
    cost, current, i = heapq.heappop(q)
    if visited[current]:
        continue

    visited[current] = True
    used[i] = True
    connect += 1

    for nx, nx_cost, nx_i in edge[current]:
        if not visited[nx]:
            heapq.heappush(q, (nx_cost, nx, nx_i))

ans = 0
for i in range(n):
    for _, cost, idx in edge[i]:
        if cost > 0 and not used[idx]:
            ans += cost

print(ans // 2)
