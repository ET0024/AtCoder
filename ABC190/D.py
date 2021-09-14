import math

n = int(input())

# (m+1) + (m+2) + ... + n = (n-m)(n+m+1)/2 = N
# 2N = (n-m)(n+m+1) -> 差が(2m+1)
# →2Nのを偶数×奇数に分割する場合の数

n = 2 * n
count = 0
for i in range(1, int(math.sqrt(n)) + 1):

    if n % i == 0:
        j = n // i
        if i % 2 + j % 2 == 1:
            count += 2  # 偶奇を考慮

print(count)
