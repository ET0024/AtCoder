n, m = map(int, input().split())
h = list(map(int, input().split()))

is_good = [True for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if h[a] >= h[b]:
        is_good[b] = False
    if h[a] <= h[b]:
        is_good[a] = False

print(is_good.count(True))
