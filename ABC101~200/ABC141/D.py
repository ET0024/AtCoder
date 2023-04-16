import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
an = list(map(lambda x: x * (-1), a))

heapq.heapify(an)

for _ in range(m):
    item = heapq.heappop(an)
    heapq.heappush(an, -(-item // 2))

print(-sum(an))
