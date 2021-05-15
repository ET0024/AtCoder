from collections import deque

H, W = map(int, input().split())
graph = [list(input()) for _ in range(H)]
visited = [[False] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if graph[i][j] == 's':
            si, sj = i, j
        elif graph[i][j] == 'g':
            gi, gj = i, j

q = deque()
q.append((si, sj))

while len(q) > 0:
    i, j = q.pop()
    visited[i][j] = True

    for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if i2 < 0 or i2 >= H or j2 < 0 or j2 >= W:
            continue
        if graph[i2][j2] != '#' and not visited[i2][j2]:
            q.append((i2, j2))

if visited[gi][gj]:
    print('Yes')
else:
    print('No')
