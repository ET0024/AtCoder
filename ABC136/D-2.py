s = input()
n = len(s)

# dp[k][i] for position of ith person after 2^k-th move (doubling)
dp = [[-1] * n for _ in range(21)]

# initial move
for i in range(n):
    if s[i] == 'R':
        dp[0][i] = i + 1
    elif s[i] == 'L':
        dp[0][i] = i - 1

# doubling for k >= 1
for k in range(1, 21):
    for i in range(n):
        dp[k][i] = dp[k - 1][dp[k - 1][i]]

count = [0 for _ in range(n)]
for val in dp[-1]:
    count[val] += 1

print(*count)
