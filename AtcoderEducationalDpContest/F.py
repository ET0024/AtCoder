from collections import deque

s = input()
t = input()

ls = len(s)
lt = len(t)

dp = [[0] * lt for _ in range(ls)]
for i in range(ls):
    for j in range(lt):
        if s[i] == t[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

q = deque()
q.append((ls - 1, lt - 1))
ans = []
while len(q) > 0:
    i, j = q.pop()

    if i == 0 and j == 0:
        if s[i]==t[j]:
            ans.append(s[i])
        break
    if i - 1 >= 0 and j - 1 >= 0 and dp[i - 1][j - 1]==dp[i][j]-1:
        ans.append(s[i])
        q.append((i - 1, j - 1))
    elif i - 1 >= 0 and dp[i - 1][j] == dp[i][j]:
        q.append((i - 1, j))
    elif j - 1 >= 0 and dp[i][j - 1] == dp[i][j]:
        q.append((i, j - 1))

print(dp)
print(ans[::-1])

0 1 1 1 1
0 1 1 2 2