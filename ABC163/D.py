n, k = map(int, input().split())


def g(m):
    return m * n - m * (m - 1) + 1


ans = 0
MOD = 10 ** 9 + 7
for i in range(k, n + 2):
    ans += g(i)
    ans %= MOD

print(ans)
# f(n) := n(n+1)/2
# 1個選ぶ -> BIG ~ BIG+N : N+1個
# 2個選ぶ -> 2*BIG + f(1) ~ 2*BIG + 2N - f(1)：2N - 2*f(1) + 1
# 3個選ぶ -> 3*BIG + f(2) ~ 3*BIG + 3N - f(2)：3N - 2*f(2) + 1
# 4個選ぶ -> 4*BIG + f(3) ~ 4*BIG + 4N - f(3)：4N - 2*f(3) + 1
