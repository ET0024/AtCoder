n = int(input())
s = [input() for _ in range(n)]

# dp[n][1(true)/0(false)]
dp = [[0] * 2 for _ in range(n + 1)]
dp[0][1] = 1
dp[0][0] = 1
for i in range(1, n + 1):
    if s[i - 1] == 'AND':
        dp[i][1] = dp[i - 1][1]
        dp[i][0] = dp[i - 1][0] * 2 + dp[i - 1][1]
    elif s[i - 1] == 'OR':
        dp[i][1] = dp[i - 1][1] * 2 + dp[i - 1][0]
        dp[i][0] = dp[i - 1][0]

print(dp[-1][1])
