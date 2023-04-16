import heapq

n, k = map(int, input().split())
a = list(map(int, input().split()))

q = [0]
ans = []
while len(q) > 0:
    val = heapq.heappop(q)
    if len(ans) > 0 and ans[-1] == val:
        continue
    ans.append(val)
    for _a in a:
        heapq.heappush(q, val + _a)
    if len(ans) > k:
        break

print(ans[k])
