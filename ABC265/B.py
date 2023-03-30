from collections import defaultdict

n, m, t = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(int)
for _ in range(m):
    x, y = map(int, input().split())
    d[x - 1] = y

life = t
for now in range(n - 1):
    life = life + d[now] - a[now]
    if life <= 0:
        print('No')
        exit()

print('Yes')
