from collections import deque

h, w = map(int, input().split())
board = []
for _ in range(h):
    board.append(list(input()))

for i in range(h):
    for j in range(w):
        if board[i][j] == 's':
            si, sj = i, j
        elif board[i][j] == 'g':
            gi, gj = i, j

reached = [[False] * w for _ in range(h)]
q = deque()
q.append((si, sj))

while len(q) > 0:
    i, j = q.popleft()
    if reached[i][j]:
        continue
    reached[i][j] = True
    for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
            continue
        if board[i2][j2] != '#':
            q.append((i2, j2))

if reached[gi][gj]:
    print('Yes')
else:
    print('No')
