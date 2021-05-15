n, W = map(int, input().split())
w = []
v = []
for _ in range(n):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)

# dp[i][v] represents the minimum weight to gain value v from item 1 ... i
dp = [[float('inf')] * (n * 1000 + 1) for _ in range(n)]
dp[0][0] = 0
dp[0][v[0]] = w[0]

for i in range(1, n):
    for k in range(n * 1000 + 1):
        if k - v[i] >= 0:
            dp[i][k] = min(dp[i - 1][k], dp[i - 1][k - v[i]] + w[i])
        else:
            dp[i][k] = dp[i - 1][k]

ans = 0
for k in range(n*1000+1):
    if dp[-1][k] <= W:
        ans = k

print(ans)