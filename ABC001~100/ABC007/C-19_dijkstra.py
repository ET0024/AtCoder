import heapq

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for _ in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

q = []

dist = [[float('inf')] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dist[sy][sx] = 0
heapq.heappush(q, (0, sy, sx))

while len(q) > 0:
    cost, y, x = heapq.heappop(q)
    if visited[y][x]:
        continue
    visited[y][x] = True
    for y2, x2 in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if y2 < 0 or y2 >= R or x2 < 0 or x2 >= C:
            continue
        if not visited[y2][x2] and c[y2][x2] != '#':
            if dist[y2][x2] > cost + 1:
                dist[y2][x2] = cost + 1
                heapq.heappush(q, (cost + 1, y2, x2))

print(dist[gy][gx])
