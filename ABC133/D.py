n = int(input())
a = list(map(int, input().split()))
yama = [0 for _ in range(n)]

# calc yama[0]
for i in range(n):
    if i % 2 == 0:
        yama[0] += a[i]
    else:
        yama[0] -= a[i]

# calc yama[1] ~ yama[n-1]
for i in range(1, n):
    yama[i] = a[i - 1] * 2 - yama[i - 1]

print(*yama)

# a[0] = (yama[0] + yama[1])/2
# a[0] - a[1] = (yama[0] - yama[2])/2
# a[0] - a[1] + a[2] = (yama[0] + yama[3])/2
# a[0] - a[1] + a[2] - a[3] = (yama[0] - yama[4])/2
# a[0] - a[1] + a[2] - a[3] + a[4] = yama[0]
