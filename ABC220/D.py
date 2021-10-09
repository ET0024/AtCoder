n = int(input())
a = list(map(int, input().split()))
MOD = 998244353
dp = [[0] * 10 for _ in range(n)]
dp[0][a[0] % 10] = 1
for i in range(1, n):
    for d in range(10):
        dp[i][(d + a[i]) % 10] += dp[i - 1][d]
        dp[i][(d + a[i]) % 10] %= MOD
        dp[i][(d * a[i]) % 10] += dp[i - 1][d]
        dp[i][(d * a[i]) % 10] %= MOD

for val in dp[-1]:
    print(val % MOD)
