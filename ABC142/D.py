from collections import defaultdict
import math

a, b = map(int, input().split())
c = math.gcd(a, b)
r = c
cf = defaultdict(int)
cf[1] = 1
for div in range(2, c + 1):
    if div ** 2 > c:
        break

    while r % div == 0:
        r //= div
        cf[div] += 1

if r > 1:
    cf[r] += 1

print(len(cf.keys()))
