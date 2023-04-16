import math

p = int(input())
f = [math.factorial(i) for i in range(1, 11)]

count = 0
for i in range(9, -1, -1):
    count += p // f[i]
    p -= f[i] * (p // f[i])

print(count)
