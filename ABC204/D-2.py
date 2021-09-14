n = int(input())
t = list(map(int, input().split()))

dp = [[False] * (10 ** 5 + 1) for _ in range(n)]

dp[0][0] = True
dp[0][t[0]] = True
for i in range(n - 1):
    for j in range(10 ** 5 + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
            dp[i + 1][j + t[i]] = True

total = sum(t)
ans = float('inf')
for val, possible in enumerate(dp[-1]):
    if possible:
        if max(val, total - val) < ans:
            ans = max(val, total - val)
print(ans)
