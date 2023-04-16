n = int(input())
a = list(map(int, input().split()))

MOD = 10 ** 9 + 7

print((sum(a) ** 2 - sum(map(lambda x: x ** 2, a))) // 2 % MOD)
