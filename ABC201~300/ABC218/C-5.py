n = int(input())
S = [list(input()) for _ in range(n)]
T = [list(input()) for _ in range(n)]

scount = 0
tcount = 0
for i in range(n):
    for j in range(n):
        if S[i][j] == '#':
            scount += 1
        if T[i][j] == '#':
            tcount += 1

if scount != tcount:
    print('No')
    exit()

for _ in range(4):
    # find left-top
    si, sj, ti, tj = n, n, n, n
    for i in range(n):
        for j in range(n):
            if S[i][j] == '#':
                si = min(si, i)
                sj = min(sj, j)
            if T[i][j] == '#':
                ti = min(ti, i)
                tj = min(tj, j)

    # judge
    flag = True
    for i in range(n):
        for j in range(n):
            if i + si < n and j + sj < n and i + ti < n and j + tj < n:
                if S[i + si][j + sj] != T[i + ti][j + tj]:
                    flag = False

    if flag:
        print('Yes')
        exit()

    # rotate
    T2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for (j) in range(n):
            T2[i][j] = T[j][n - 1 - i]
    T = T2

print('No')
exit()
