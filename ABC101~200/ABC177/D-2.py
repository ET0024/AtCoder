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
gid = 0

for i in range(n):
    # iを起点としてBFSする
    if group[i] >= 0:
        continue

    q = deque()
    q.append(i)
    while len(q) > 0:
        current = q.popleft()
        if group[current] >= 0:
            continue
        group[current] = gid
        for nx in edge[current]:
            if group[nx] < 0:
                q.append(nx)

    gid += 1

count = [0 for _ in range(n)]
for g in group:
    count[g] += 1

print(max(count))
