n = int(input())
p = list(map(int, input().split()))

dp = [[False] * (n * 100 + 1) for _ in range(n)]
dp[0][0] = True
dp[0][p[0]] = True

for i in range(1, n):
    for x in range(n * 100 + 1):
        if x - p[i] >= 0:
            dp[i][x] = dp[i - 1][x] or dp[i - 1][x - p[i]]
        else:
            dp[i][x] = dp[i - 1][x]

print(sum(dp[-1]))