from collections import deque

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

group = [-1 for _ in range(n)]
g = 0

for i in range(n):
    if group[i] >= 0:
        continue

    q = deque()
    q.append(i)
    while len(q) > 0:
        current = q.popleft()
        group[current] = g
        for nx in edge[current]:
            if group[nx] < 0:
                q.append(nx)

    g += 1

count = [0 for _ in range(n)]
for val in group:
    count[val] += 1

print(max(count))
