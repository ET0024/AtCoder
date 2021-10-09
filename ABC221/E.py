MOD = 998244353
MAX = 3 * 10 ** 5
powers = [0 for _ in range(MAX + 1)]
powers[0] = 1
for i in range(1, MAX + 1):
    powers[i] = (powers[i - 1] * 2) % MOD

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):

        if a[j] >= a[i]:
            ans += powers[j - i - 1]
            ans %= MOD

print(ans)
# a2 = []
# for i, val in enumerate(a):
#     a2.append((val, i))
# a2.sort()
# acc = [0 for _ in range(n)]
# acc[n - 1] += a2[n - 1][1]
# for i in range(n - 1, -1, -1):
#     acc[i]
# print(a)
# print(a2)
