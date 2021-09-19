import heapq

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for idx in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((c, b, idx))
    edge[b].append((c, a, idx))

visited = [False for _ in range(n)]
used = [False for _ in range(m)]
q = []
connected = 0

visited[0] = True
for cost, nxt, idx in edge[0]:
    heapq.heappush(q, (cost, nxt, idx))

while len(q) > 0 and connected < n:
    cost, nxt, idx = heapq.heappop(q)
    if visited[nxt]:
        continue
    visited[nxt] = True
    used[idx] = True
    connected += 1

    for cost2, nxt2, idx2 in edge[nxt]:
        if not visited[nxt2] and not used[idx2]:
            heapq.heappush(q, (cost2, nxt2, idx2))

ans = 0
for node in range(n):
    for cost, nxt, idx in edge[node]:
        if not used[idx] and cost > 0:
            ans += cost

print(ans // 2)
