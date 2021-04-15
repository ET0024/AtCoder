N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)

# dp[i][k]: i番目までの品物で重さ丁度kのときの最大価値
dp = [[0] * (W + 1) for _ in range(N)]

for i in range(N):
    for k in range(W + 1):
        if i == 0:
            if k == w[i]:
                dp[i][k] = v[i]
            else:
                dp[i][k] = 0
            continue

        if k >= w[i]:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - w[i]] + v[i])
        else:
            dp[i][k] = dp[i - 1][k]

ans = 0
for k in range(W + 1):
    if dp[-1][k] > ans:
        ans = dp[-1][k]

print(ans)
