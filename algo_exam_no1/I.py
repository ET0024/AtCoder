n, m = map(int, input().split())
s = []
c = []
for _ in range(m):
    _s, _c = input().split()

    tmp = 0
    for i in range(n):
        if _s[i] == 'Y':
            tmp |= 1 << i
    s.append(tmp)
    c.append(int(_c))

ALL = 1 << n
# dp[i][pattern] represents the minimum cost for given pattern within ith items
dp = [[float('inf')] * ALL for _ in range(m)]

for i in range(m):
    pattern = s[i]
    cost = c[i]

    if i == 0:
        dp[0][0] = 0
        dp[0][pattern] = cost
    else:
        for j in range(ALL):
            # notice: cannot describe both pattern (buy or not buy) at once
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            dp[i][j | pattern] = min(dp[i][j | pattern], dp[i - 1][j] + cost)

ans = dp[-1][-1]
if ans == float('inf'):
    print(-1)
else:
    print(ans)

for r in dp:
    print(r[-1])