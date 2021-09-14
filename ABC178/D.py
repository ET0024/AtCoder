# 3 -> (3)
# 4 -> (4)
# 5 -> (5)
# 6 -> (6), (3, 3)
# 7 -> (7), (4, dp(3)), (3, dp(4))
# 8 -> (8, dp(0)), (5, dp(3)), (4, dp(4)), (3, dp(5))

s = int(input())

MOD = 10 ** 9 + 7
dp = [0 for _ in range(2001)]
dp[0] = 1
dp[1] = 0
dp[2] = 0

for i in range(3, s + 1):
    for j in range(3, i + 1):
        dp[i] = (dp[i] + dp[i - j]) % MOD

print(dp[s])

