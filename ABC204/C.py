from collections import deque

n, m = map(int, input().split())
edge = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)

ans = 0
for start in range(n):
    q = deque()
    q.append(start)
    visited = [False for _ in range(n)]

    while len(q) > 0:
        current = q.pop()
        if visited[current]:
            continue
        visited[current] = True
        ans += 1
        for nxt in edge[current]:
            if not visited[nxt]:
                q.append(nxt)

print(ans)