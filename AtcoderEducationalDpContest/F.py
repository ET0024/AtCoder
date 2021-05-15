from collections import deque

s = input()
t = input()

ls = len(s)
lt = len(t)

dp = [[0] * (lt + 1) for _ in range(ls + 1)]
for i in range(0, ls):
    for j in range(1, lt):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
ans = []
pos = (ls, lt)
while pos != (0, 0):

    i, j = pos[0], pos[1]
    if i - 1 >= 0 and j - 1 >= 0 and dp[i - 1][j - 1] == dp[i][j] - 1:
        ans.append(s[i - 1])
        pos = (pos[0] - 1, pos[1] - 1)
    elif i - 1 >= 0 and dp[i - 1][j] == dp[i][j]:
        pos = (pos[0] - 1, pos[1])
    elif j - 1 >= 0 and dp[i][j - 1] == dp[i][j]:
        pos = (pos[0], pos[1] - 1)

if s[0] == t[0]:
    ans.append(s[0])
print(''.join(ans[::-1]))
# print('-------------------')
# print(' ' + str(list(' ' + t)))
# for i, r in enumerate(dp):
#     print((' ' + s)[i], r)
# print('-------------------')
