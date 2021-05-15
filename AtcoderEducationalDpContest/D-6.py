N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)

dp = [[0] * (W + 1) for _ in range(N)]
dp[0][0] = 0
dp[0][w[0]] = v[0]
for item in range(1, N):
    for weight in range(W + 1):
        if weight - w[item] >= 0:
            dp[item][weight] = max(dp[item - 1][weight], dp[item - 1][weight - w[item]] + v[item])
        else:
            dp[item][weight] = dp[item - 1][weight]

print(max(dp[-1]))
