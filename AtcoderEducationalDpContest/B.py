n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    for step in range(1, k+1):
        if i + step < n:
            tmp = dp[i] + abs(h[i + step] - h[i])
            if dp[i + step] > tmp:
                dp[i + step] = tmp

print(dp[-1])
