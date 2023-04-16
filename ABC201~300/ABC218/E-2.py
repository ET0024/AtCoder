import heapq

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c, i))
    edge[b].append((a, c, i))

used = [False for _ in range(m)]
visited = [False for _ in range(n)]
cnt = 0

q = []
visited[0] = True
for nx, cost, idx in edge[0]:
    heapq.heappush(q, (cost, nx, idx))

while len(q) > 0 and cnt < n:
    cost, current, idx = heapq.heappop(q)
    if visited[current]:
        continue
    used[idx] = True
    visited[current] = True
    cnt += 1

    for nx, nx_cost, nx_idx in edge[current]:
        if not visited[nx]:
            heapq.heappush(q, (nx_cost, nx, nx_idx))

ans = 0
for i in range(n):
    for nx, cost, idx in edge[i]:
        if not used[idx] and cost > 0:
            ans += cost

print(ans // 2)
