from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

sy -= 1
sx -= 1
gy -= 1
gx -= 1
dist = [[-1] * c for _ in range(r)]
dist[sy][sx] = 0
q = deque()
q.append((sy, sx))

while len(q) > 0:
    y, x = q.popleft()
    for y2, x2 in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if y2 < 0 or y2 >= r or x2 < 0 or x2 >= c:
            continue
        if board[y2][x2] == '#' or dist[y2][x2] >= 0:
            continue
        dist[y2][x2] = dist[y][x] + 1
        q.append((y2, x2))

print(dist[gy][gx])
