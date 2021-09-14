n = int(input())
t = list(map(int, input().split()))

# dp[i][t]: possible time diff t with first ith items
MAX = 1000 * n
dp = [[False] * (2 * MAX + 1) for _ in range(n)]

dp[0][MAX + t[0]] = True
dp[0][MAX - t[0]] = True

for i in range(1, n):
    for j in range(2 * MAX + 1):
        for diff in [t[i], -t[i]]:
            if 0 <= j + diff < 2 * MAX + 1:
                dp[i][j + diff] = dp[i][j + diff] or dp[i - 1][j]
    # print(i, dp[i].count(True))

target = -1
for diff in range(MAX + 1):
    if dp[-1][MAX + diff] or dp[-1][MAX - diff]:
        target = diff
        break
print((sum(t) - target)//2 + target)

