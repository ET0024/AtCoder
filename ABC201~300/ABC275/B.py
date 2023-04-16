x = list(map(int, input().split()))
MOD = 998244353
x = list(map(lambda x: x % MOD, x))
print((x[0] * x[1] * x[2] - x[3] * x[4] * x[5]) % MOD)
