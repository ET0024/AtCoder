# MLE code

import heapq

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            si = i
            sj = j
        elif c[i][j] == 'g':
            gi = i
            gj = j

dist = [[float('inf')] * w for _ in range(h)]
visited = [[False] * w for _ in range(h)]
q = [(0, si, sj)]
dist[si][sj] = 0

# dijkstra
while len(q) > 0:
    cost, i, j = heapq.heappop(q)
    if visited[i][j]:
        continue

    for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
            continue

        # adjacent move
        if c[i2][j2] != '#' and cost < dist[i2][j2]:
            dist[i2][j2] = cost
            heapq.heappush(q, (cost, i2, j2))

        # illegal move
        if c[i2][j2] == '#' and cost + 1 < dist[i2][j2]:
            dist[i2][j2] = cost + 1
            heapq.heappush(q, (cost + 1, i2, j2))

if dist[gi][gj] <= 2:
    print('YES')
else:
    print('NO')
