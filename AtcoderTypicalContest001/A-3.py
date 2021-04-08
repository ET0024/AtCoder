from collections import deque

H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]

for i in range(W):
    for j in range(H):
        if c[j][i] == 's':
            sy = j
            sx = i
        elif c[j][i] == 'g':
            gy = j
            gx = i

dist = [[-1] * W for _ in range(H)]
q = deque()

dist[sy][sx] = 0
q.append((sy, sx))
while len(q) > 0:
    y, x = q.popleft()

    for y2, x2 in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if y2 < 0 or y2 >= H or x2 < 0 or x2 >= W:
            continue
        if dist[y2][x2] < 0 and c[y2][x2] != '#':
            dist[y2][x2] = dist[y][x] + 1
            q.append((y2, x2))

if dist[gy][gx] > 0:
    print('Yes')
else:
    print('No')
