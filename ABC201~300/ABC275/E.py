n, m, k = map(int, input().split())

dp = [[0] * (k+1) for _ in range(n + 1)]
dp[0][0] = 1
MOD = 998244353
for i in range(0, n):
    for _k in range(0, k):
        for step in range(1, m + 1):
            if i+step <= n:
                dp[i+step][_k+1] += dp[i][_k]

# calc x
x = 1
for _ in range(k):
    x *= m
    x %= MOD

# calc y
y = 0
for i in range(k+1):
    y += dp[n-m][i]*(m**(k-i)-(m-1)**(k-1))
    y %= MOD


print(y)
print(x)


