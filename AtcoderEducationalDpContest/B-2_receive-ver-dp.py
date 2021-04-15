n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    for step in range(1, k + 1):
        if i - step >= 0:
            tmp = dp[i - step] + abs(h[i] - h[i - step])
            if dp[i] > tmp:
                dp[i] = tmp

print(dp[-1])
