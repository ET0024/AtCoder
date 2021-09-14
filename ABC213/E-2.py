import heapq

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

dist = [[float('inf')] * w for _ in range(h)]
visited = [[False] * w for _ in range(h)]

dist[0][0] = 0
q = [(0, 0, 0)]

while len(q) > 0:
    cost, i, j = heapq.heappop(q)
    if visited[i][j]:
        continue
    visited[i][j] = True

    # adjacent node
    for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
            continue
        if not visited[i2][j2] and s[i2][j2] != '#' and cost < dist[i2][j2]:
            dist[i2][j2] = cost
            heapq.heappush(q, (cost, i2, j2))

    # move with punch
    for di in range(-2, 3):
        for dj in range(-2, 3):
            if abs(di) + abs(dj) == 4:
                continue
            i2 = i + di
            j2 = j + dj
            if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
                continue
            if not visited[i2][j2] and cost + 1 < dist[i2][j2]:
                dist[i2][j2] = cost + 1
                heapq.heappush(q, (cost + 1, i2, j2))

print(dist[-1][-1])
