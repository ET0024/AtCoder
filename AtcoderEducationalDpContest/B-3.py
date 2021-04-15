N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf')]*N
dp[0]=0

for n in range(N):
    for k in range(1, K+1):
        if n-k>=0:
            dp[n] = min(dp[n], dp[n-k]+abs(h[n]-h[n-k]))

print(dp[-1])