n = int(input())
S = [list(input()) for _ in range(n)]
T = [list(input()) for _ in range(n)]

s = set()
t = set()
for i in range(n):
    for j in range(n):
        if S[i][j] == '#':
            s.add((i, j))
        if T[i][j] == '#':
            t.add((i, j))

for _ in range(4):

    # horizontal/vertical move
    si, sj = min(s)
    ti, tj = min(t)
    t_adjust = set((i - ti + si, j - tj + sj) for i, j in t)

    # check
    if s == t_adjust:
        print('Yes')
        exit()

    # rotate t
    t = [(-j, i) for i, j in t]

print('No')
