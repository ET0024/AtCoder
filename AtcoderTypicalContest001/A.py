from collections import deque

H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]

sy, sx, gy, gx = 0, 0, 0, 0
visited = [[False] * W for _ in range(H)]

for j in range(H):
    for i in range(W):
        if c[j][i] == 's':
            sy = j
            sx = i
        elif c[j][i] == 'g':
            gy = j
            gx = i

q = deque()
q.append((sy, sx))

while len(q) > 0:
    y, x = q.pop()
    visited[y][x] = True

    for y2, x2 in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if y2 < 0 or y2 >= H or x2 < 0 or x2 >= W:
            continue
        if not visited[y2][x2] and c[y2][x2] != '#':
            q.append((y2, x2))

if visited[gy][gx]:
    print('Yes')
else:
    print('No')
