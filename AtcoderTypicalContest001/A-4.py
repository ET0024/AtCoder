import sys

sys.setrecursionlimit(10 ** 6)
H, W = map(int, input().split())
graph = [list(input()) for _ in range(H)]
reached = [[False] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if graph[i][j] == 's':
            si, sj = i, j
        elif graph[i][j] == 'g':
            gi, gj = i, j

reached[si][sj] = True


def dfs(now):
    i, j = now
    reached[i][j] = True
    for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if i2 < 0 or i2 >= H or j2 < 0 or j2 >= W:
            continue
        if graph[i2][j2] == '#':
            continue
        if not reached[i2][j2]:
            dfs((i2, j2))


dfs((si, sj))

if reached[gi][gj]:
    print('Yes')
else:
    print('No')
