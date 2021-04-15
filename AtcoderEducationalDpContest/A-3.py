N = int(input())
h = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0

for i in range(1, N):
    if i-2>=0:
        dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))
    else:
        dp[i] = dp[i-1]+abs(h[i]-h[i-1])

print(dp[-1])