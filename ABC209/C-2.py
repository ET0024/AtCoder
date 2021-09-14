n = int(input())
c = list(map(int, input().split()))

MOD = 10 ** 9 + 7

c.sort()
total = 1
for i, val in enumerate(c):
    total *= val - i
    total %= MOD

print(total % MOD)
