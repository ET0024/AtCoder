N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)

V = 10 ** 3 + 1
dp = [[float('inf')] * V * N for _ in range(N)]
dp[0][0] = 0
dp[0][v[0]] = w[0]

for i in range(1, N):
    for x in range(V * N):

        if x - v[i] >= 0:
            dp[i][x] = min(dp[i - 1][x], dp[i - 1][x - v[i]] + w[i])
        else:
            dp[i][x] = dp[i - 1][x]

ans = 0
for val, x in enumerate(dp[-1]):
    if x <= W and val > ans:
        ans = val
print(ans)
