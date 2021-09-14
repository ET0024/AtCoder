n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
dp = [0 for _ in range(n)]  # dp[i]:右端がiのsum of difference
dp[0] = 0
for i, val in enumerate(a):
    if i == 0:
        continue
    dp[i] = dp[i - 1] + (a[i] - a[i - 1]) * i

print(sum(dp))