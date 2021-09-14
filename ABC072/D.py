n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(n - 1):
    if p[i] == i + 1:
        p[i], p[i + 1] = p[i + 1], p[i]
        count += 1

if p[n - 1] == n:
    p[n - 2], p[n - 1] = p[n - 1], p[n - 2]
    count += 1

print(count)
