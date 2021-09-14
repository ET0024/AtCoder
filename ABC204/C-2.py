from collections import deque

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)

count = 0
for s in range(n):
    q = deque()
    visited = [False for _ in range(n)]
    q.append(s)
    while len(q) > 0:
        current = q.popleft()
        visited[current] = True

        for nx in edge[current]:
            if not visited[nx]:
                q.append(nx)

    count += visited.count(True)

print(count)
