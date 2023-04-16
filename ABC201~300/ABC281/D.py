n, k, d = map(int, input().split())
a = list(map(int, input().split()))

# dp[n][k][d] = index=nまでの部分数列からk個選んだときにmodがdになる場合の最大値
INF = 1E10
dp = [[[-INF] * d for _ in range(k + 1)] for _ in range(n)]

for n2 in range(n):
    for d2 in range(d):
        dp[n2][0][d2] = 0

dp[0][1][a[0] % d] = a[0]

for n2 in range(1, n):
    print('debugehiere', n2)
    for k2 in range(1, min(n2+2, k + 1)):
        for d2 in range(d):
            dp[n2][k2][d2] = max(dp[n2 - 1][k2][d2], dp[n2 - 1][k2 - 1][(d2 - a[n2]) % d] + a[n2])
            print('*** dp=', dp[n2][k2][d2], "ord=", n2, k2, d2)

print(dp[-1][k][0])

print('----------')
print(dp[0])
print(dp[1])
print(dp[2])
print(dp[3])
