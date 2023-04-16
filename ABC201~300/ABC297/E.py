import heapq

n, k = map(int, input().split())
a = list(map(int, input().split()))

q = [0]
ans = []
current_max = -1
while len(q) > 0:
    val = heapq.heappop(q)
    if val == current_max:
        continue
    current_max = val
    ans.append(val)
    for _a in a:
        heapq.heappush(q, _a + val)
    if len(ans) > k:
        break

print(ans[k])
