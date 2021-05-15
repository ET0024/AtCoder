n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(1, n):
    for d in range(k + 1):
        if i - d >= 0:
            dp[i] = min(dp[i], dp[i - d] + abs(h[i] - h[i - d]))

print(dp[-1])
