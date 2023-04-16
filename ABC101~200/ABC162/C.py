import math

k = int(input())

ans = 0

gcd_result = [0 for _ in range(k + 1)]
for i in range(1, k + 1):
    for j in range(1, k + 1):
        gcd_result[math.gcd(i, j)] += 1

ans = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        ans += math.gcd(i, j) * gcd_result[i]

print(ans)
#
# # gcdを予め計算
# g_cash = [[0] * (k + 1) for _ in range(k + 1)]
# for i in range(1, k + 1):
#     for j in range(1, k + 1):
#         g_cash[i][j] = math.gcd(i, j)
#
# for a in range(1, k + 1):
#     for b in range(1, k + 1):
#         for c in range(1, k + 1):
#             ans += g_cash[a][g_cash[b][c]]
#             # ans += math.gcd(a, math.gcd(b, c))
#
# print(ans)
