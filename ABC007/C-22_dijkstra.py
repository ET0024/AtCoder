import heapq

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1
c = [list(input()) for _ in range(R)]

q = []
dist = [[-1] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dist[sy][sx] = 0
heapq.heappush(q, (0, sy, sx))

while len(q) > 0:
    cost, y, x = heapq.heappop(q)
    if visited[y][x]:
        continue
    dist[y][x] = cost
    visited[y][x] = True
    for y2, x2 in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if visited[y2][x2] or c[y2][x2] == '#':
            continue
        heapq.heappush(q, (cost + 1, y2, x2))

print(dist[gy][gx])
