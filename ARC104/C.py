n = int(input())
a, b = [], []

for i in range(n):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)

dp = [False] * n  # 区間の始点になり得るノードかどうか
dp[0] = True

for i in range(n):

    if dp[i] == True:
        for j in range(i, n):
            _a = a[2*i:2*j]
            _b = b[2*i:2*j]
    else:
        continue

    # if possible in 2*i
    dp[i] = True
