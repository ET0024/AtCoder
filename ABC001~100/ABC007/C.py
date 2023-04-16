from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sx -= 1
sy -= 1
gy -= 1
gx -= 1

graph = [list(input()) for _ in range(r)]
dist = [[-1] * c for _ in range(r)]
q = deque()

dist[sy][sx] = 0
q.append((sy, sx))

while len(q) > 0:
    y, x = q.popleft()

    for y2, x2 in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if x2 < 0 or x2 > c + 1 or y2 < 0 or y2 > r + 1:
            continue

        if graph[y2][x2] == '#':
            continue

        if dist[y2][x2] == -1:
            dist[y2][x2] = dist[y][x] + 1
            q.append((y2, x2))

print(dist[gy][gx])
