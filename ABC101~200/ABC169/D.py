n = int(input())

# 素因数分解
factors = []
res = n

for p in range(2, n):
    if p ** 2 > n:
        break

    count = 0
    while res % p == 0:
        res //= p
        count += 1
    if count > 0:
        factors.append((p, count))

if res > 1:
    factors.append((res, 1))

ans = 0
for p, count in factors:
    x = 1
    while count - x >= 0:
        ans += 1
        count -= x
        x += 1

print(ans)
