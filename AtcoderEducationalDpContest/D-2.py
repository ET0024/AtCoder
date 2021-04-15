N, W = map(int, input().split())
w = []
v = []

for _ in range(N):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)

# dp[i][k] := i番目までの品物、重さk以下で最大の価値

dp = [[0] * (W + 1) for _ in range(N)]


for i in range(N):
    for k in range(W + 1):
        if i == 0:
            if k < w[i]:
                dp[i][k] = 0
            else:
                dp[i][k] = v[i]
            continue

        if k-w[i]>=0:
            dp[i][k]=max(dp[i-1][k], dp[i-1][k-w[i]]+v[i])
        else:
            dp[i][k] = dp[i - 1][k]

print(dp[-1][-1])