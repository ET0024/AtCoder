import heapq

n, m, q = map(int, input().split())
item = []
for _ in range(n):
    w, v = map(int, input().split())
    heapq.heappush(item, (-v, w))

x = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if r == m - 1:
        x2 = x[:l]
    else:
        x2 = x[:l] + x[r + 1:]
    x2.sort()
    used = [False for _ in range(len(x2))]
    item2 = item.copy()

    ans = 0
    while len(item2) > 0:
        v, w = heapq.heappop(item2)
        v = -v
        for i, size in enumerate(x2):
            if w <= size and not used[i]:
                ans += v
                used[i] = True
                # print('debug:', size, v, '-packed')
                break
    print(ans)
