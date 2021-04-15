N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)

# dp[n][v]:n番目の品物で、価値vを達成できる最小の重さ

dp = [[float('inf')] * (N * 1000 + 1) for _ in range(N)]

for i in range(N):
    for k in range(N * 1000 + 1):
        if i == 0:
            if k == 0:
                dp[i][k] = 0
            elif k == v[i]:
                dp[i][k] = w[i]
            else:
                pass
            continue

        if k - v[i] >= 0:
            dp[i][k] = min(dp[i - 1][k], dp[i - 1][k - v[i]] + w[i])
        else:
            dp[i][k] = dp[i - 1][k]

ans = 0
for k in range(N * 1000 + 1):
    if dp[-1][k] <= W:
        ans = max(ans, k)

print(ans)
