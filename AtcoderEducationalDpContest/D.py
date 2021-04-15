N, W = map(int, input().split())

w = []
v = []
for _ in range(N):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)

# dp[n][w]
dp = [[0] * (W + 1) for _ in range(N)]

for i in range(N):
    for k in range(W + 1):
        if k - w[i] >= 0:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - w[i]] + v[i])
        else:
            dp[i][k] = dp[i - 1][k]

print(dp[-1][-1])
