n, d = map(int, input().split())
t = list(map(int, input().split()))

current = t[0]
pre = 0
for i in range(1, n):
    pre, current = current, t[i]
    if current - pre <= d:
        print(current)
        exit()

print(-1)
