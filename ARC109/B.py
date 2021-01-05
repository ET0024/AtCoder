import math

n = int(input())
m = int(-1 / 2 + math.sqrt(2 * (n + 1) + 1 / 4))

if m * (m + 1) > 2 * (n + 1):
    m -= 1

print(n - m + 1)
