s = input()
n = len(s)

# doubling: dp[k][i] for position after 2^k move

dp = [[0] * n for _ in range(21)]

for i in range(n):
    if s[i] == 'R':
        dp[0][i] = i + 1
    else:
        dp[0][i] = i - 1

for k in range(1, 21):
    for i in range(n):
        dp[k][i] = dp[k - 1][dp[k - 1][i]]

count = [0 for _ in range(n)]
for goal in dp[-1]:
    count[goal] += 1

print(*count)
