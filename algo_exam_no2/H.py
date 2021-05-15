n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(input()))

dp = [[float('inf')] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            a[i][j] = '0'
            dp[i][j] = 0
        elif a[i][j] == 'G':
            a[i][j] = '10'
            gi, gj = i, j

for i in range(n):
    a[i] = list(map(int, a[i]))

for score in range(11):
    for i in range(n):
        for j in range(m):
            if a[i][j] == score:
                for ii in range(n):
                    for jj in range(m):
                        if a[ii][jj] == score - 1:
                            dp[i][j] = min(dp[i][j], dp[ii][jj] + abs(i - ii) + abs(j - jj))

if dp[gi][gj] == float('inf'):
    print(-1)
else:
    print(dp[gi][gj])
