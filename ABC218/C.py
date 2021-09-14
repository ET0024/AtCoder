n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]


def process(s, t):
    s_imin = float('inf')
    s_jmin = float('inf')
    t_imin = float('inf')
    t_jmin = float('inf')
    scount = 0
    tcount = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                scount += 1
                s_imin = min(s_imin, i)
                s_jmin = min(s_jmin, j)
            if t[i][j] == '#':
                tcount += 1
                t_imin = min(t_imin, i)
                t_jmin = min(t_jmin, j)
    if scount != tcount:
        print('No')
        exit()
    
    s_offset = (s_imin, s_jmin)
    t_offset = (t_imin, t_jmin)

    unmatch = False
    for i in range(n):
        for j in range(n):
            if s_offset[0] + i >= n or s_offset[1] + j >= n:
                continue
            if t_offset[0] + i >= n or t_offset[1] + j >= n:
                continue

            if s[s_offset[0] + i][s_offset[1] + j] != t[t_offset[0] + i][t_offset[1] + j]:
                unmatch = True

    if not unmatch:
        print('Yes')
        exit()


t1 = [[0] * n for _ in range(n)]
t2 = [[0] * n for _ in range(n)]
t3 = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        t1[i][j] = t[n - 1 - j][i]
        t2[i][j] = t[n - 1 - i][n - 1 - j]
        t3[i][j] = t[j][n - 1 - i]

# for r in t:
#     print(''.join(r))
# print('-------------------------')
# for r in t1:
#     print(''.join(r))
# print('-------------------------')
# for r in t2:
#     print(''.join(r))
# print('-------------------------')
# for r in t3:
#     print(''.join(r))
# print('-------------------------')


process(s, t)
process(s, t1)
process(s, t2)
process(s, t3)
print('No')
