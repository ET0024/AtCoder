from collections import deque

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = 0
for si in range(h):
    for sj in range(w):
        if s[si][sj] == '#':
            continue
        dist = [[-1] * w for _ in range(h)]
        q = deque()
        q.append((si, sj))
        dist[si][sj] = 0

        while len(q) > 0:
            i1, j1 = q.popleft()
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if i2 < 0 or i2 >= h or j2 < 0 or j2 >= w:
                    continue
                if s[i2][j2] == '#' or dist[i2][j2] >= 0:
                    continue
                dist[i2][j2] = dist[i1][j1] + 1
                q.append((i2, j2))

        for r in dist:
            ans = max(ans, max(r))

print(ans)
