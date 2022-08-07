n = int(input())
a = list(map(int, input().split()))
INF = 10 ** 20
a.append(10 ** 9 + 1)

dp1 = [INF for _ in range(n + 1)]
dp2 = [INF for _ in range(n + 1)]

dp1[0] = a[0]
dp1[1] = a[0]
for i in range(2, n):
    dp1[i] = min(dp1[i], dp1[i - 1] + a[i - 1])
    dp1[i] = min(dp1[i], dp1[i - 1] + a[i])
    dp1[i + 1] = min(dp1[i + 1], dp1[i - 1] + a[i])

dp2[0] = a[n - 1]
for i in range(1, n):
    dp2[i] = min(dp2[i], dp2[i - 1] + a[i - 1])
    dp2[i] = min(dp2[i], dp2[i - 1] + a[i])
    dp2[i + 1] = min(dp2[i + 1], dp2[i - 1] + a[i])

print(min(dp1[n - 1], dp2[n - 2]))
