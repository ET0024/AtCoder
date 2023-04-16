from collections import defaultdict

h, w = map(int, input().split())
g = []
for _ in range(h):
    g.append(list(input()))

i, j = 0, 0
visited = defaultdict(bool)
visited[(i, j)] = True
while True:
    code = g[i][j]
    if code == 'U' and i != 0:
        i -= 1
    elif code == 'D' and i != h - 1:
        i += 1
    elif code == 'L' and j != 0:
        j -= 1
    elif code == 'R' and j != w - 1:
        j += 1
    else:
        break
    if visited[(i, j)]:
        print(-1)
        exit()
    visited[(i, j)] = True

print(i + 1, j + 1)
