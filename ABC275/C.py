import itertools

s = []
size = 9
for _ in range(size):
    s.append(list(input()))

ans = 0
sharps = []
for i in range(size):
    for j in range(size):
        if s[i][j] == '#':
            sharps.append((i, j))

for pairs in itertools.combinations(sharps, 4):
    d = []
    for i in range(3):
        for j in range(i + 1, 4):
            d.append((pairs[i][0] - pairs[j][0]) ** 2 + (pairs[i][1] - pairs[j][1]) ** 2)
    d.sort()
    ref = [d[0], d[0], d[0], d[0], 2 * d[0], 2 * d[0]]
    if d == ref:
        ans += 1

print(ans)
