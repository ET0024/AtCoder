import math

n = int(input())

sq_n = int(math.sqrt(n + 1)) + 1

score = float('inf')

for i in range(1, sq_n + 1):
    if n % i == 0:
        j = n // i
        if i + j - 2 < score:
            score = i + j - 2

print(score)
