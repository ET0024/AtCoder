n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

MOD = 998244353

# dp[i][k] for # of sequence c[0:k] that ends with value up to k
dp = [[0] * 3001 for _ in range(n)]
for val in range(a[0], b[0] + 1):
    dp[0][val] += dp[0][val - 1] + 1

for i in range(1, n):
    k = -1
    loop = True
    while k <= 3000 and loop:
        k += 1
        if k < a[i]:
            continue
        if a[i] <= k <= b[i - 1]:
            dp[i][k] = (dp[i - 1][k] + dp[i][k - 1]) % MOD
        if k > b[i - 1]:
            if k > b[i]:
                loop = False
                continue
            dp[i][k] = (dp[i][k - 1] + dp[i - 1][b[i - 1]]) % MOD

print(dp[-1][b[-1]])
