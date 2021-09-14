n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf') for _ in range(n)]
dp[0] = 0
for i in range(1, n):
    for step in range(k + 1):
        if i - step >= 0:
            dp[i] = min(dp[i], dp[i - step] + abs(h[i] - h[i - step]))

print(dp[-1])
