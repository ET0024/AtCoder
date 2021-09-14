import math
from collections import defaultdict

a, b = map(int, input().split())
c = math.gcd(a, b)

p = defaultdict(int)
p[1] = 1
r = c

for div in range(2, c + 1):
    if div ** 2 > c:
        break

    while r % div == 0:
        r //= div
        p[div] += 1

if r > 1:
    p[r] += 1

print(len(p.keys()))
