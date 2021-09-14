n, m, k = map(int, input().split())

missing = [[] for _ in range(n)]
missing2 = []
dp = [[0] * n for _ in range(k + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    missing[u].append(v)  # 片側のみ
    missing2.append((u, v))

dp[0][0] = 1
DIV = 998244353

for day in range(1, k + 1):

    # dpsum = sum(dp[day - 1]) % DIV
    dpsum = 0
    for v in dp[day - 1]:
        dpsum += v
        dpsum = dpsum % DIV

    for city in range(n):
        dp[day][city] = dpsum  # 全部足す
        dp[day][city] = (dp[day][city] - dp[day - 1][city]) % DIV  # 自分自身を引く

    for i, j in missing2:
        dp[day][i] = (dp[day][i] - dp[day - 1][j]) % DIV
        dp[day][j] = (dp[day][j] - dp[day - 1][i]) % DIV

    # for city, ngs in enumerate(missing):
    #     for neighbor in ngs:
    #         dp[day][city] -= dp[day - 1][neighbor] # NGのルートを引く
    #         dp[day][neighbor] -= dp[day - 1][city] # 反対向きも考慮

print(dp[-1][0] % DIV)
