import math

n = int(input())
a = list(map(int, input().split()))

gcd_left = [0 for _ in range(n)]
gcd_right = [0 for _ in range(n)]

gcd_left[0] = a[0]
gcd_right[n - 1] = a[n - 1]
for i in range(1, n):
    gcd_left[i] = math.gcd(gcd_left[i - 1], a[i])
    gcd_right[n - i - 1] = math.gcd(gcd_right[n - i], a[n - i - 1])

ans = 0
for blank in range(n):
    if blank == 0:
        x = gcd_right[1]
    elif blank == n - 1:
        x = gcd_left[n - 2]
    else:
        x = math.gcd(gcd_left[blank - 1], gcd_right[blank + 1])
    if x > ans:
        ans = x

print(ans)
