from collections import deque

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

q = deque()
q.append(0)
visited = [False for _ in range(n)]
ans = []
while len(q) > 0:
    current = q.pop()
    ans.append(current + 1)

    if visited[current]:
        continue
    visited[current] = True
    nxs = sorted(edge[current], reverse=True)

    for nx in nxs:
        if not visited[nx]:
            q.append(current)
            q.append(nx)

print(*ans)
