import math

a, b, n = map(int, input().split())

print(a * min(b - 1, n) // b)
# print(math.floor(a * min(b - 1, n) / b))
