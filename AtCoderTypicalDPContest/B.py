A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# dp[i][j] := 左側からi個, 右側からj取ったときのすぬけ君の最大スコア
dp = [[0] * (B + 1) for _ in range(A + 1)]
dp[0][0] = 0

# dp[1][1] = max(a[0], b[0])
# dp[2][0] = a[0]
# dp[0][2] = b[0]

for i in range(A + 1):
    for j in range(B + 1):
        if i < A and j < B:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + max(a[i], b[j]))
        if i + 1 < A:
            dp[i + 2][j] = max(dp[i + 2][j], dp[i][j] + a[i])
        if j + 1 < B:
            dp[i][j + 2] = max(dp[i][j + 2], dp[i][j] + b[j])

print(dp[-1][-1])

for r in dp:
    print(r)

#   2
# 1 10
