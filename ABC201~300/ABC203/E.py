import math
import bisect
import heapq
from collections import defaultdict

N, M = map(int, input().split())
b = []
for _ in range(M):
    x, y = map(int, input().split())
    # b.append((x, y))
    if x + y >= N - 10 or math.abs(y - x) <= N + 10:
        b.append((x, y))

b.sort()
b_dict = defaultdict(list)
b_keylist = set()

for x, y in b:
    heapq.heappush(b_dict[x], y)
    # b_dict[x].append(y)
    b_keylist.add(x)

b_keylist = list(b_keylist)
b_keylist.sort()
# print(b_dict)
# print(b_keylist)

ans = set()
ans.add(N)
upper = N

for key in b_keylist:
    upper -= 1
    ylist = b_dict[key]
    right = bisect.bisect_left(ylist, upper)
    ylist = set(ylist[right:])

    ans_plus1 = set(map(lambda x: x + 1, ans))
    ans_minus1 = set(map(lambda x: x - 1, ans))

    # ans = list((ans_0 - ylist) | (ans_plus1 & ylist) | (ans_minus1 & ylist))
    ans = (ans - ylist) | (ans_plus1 | ans_minus1) & ylist

print(len(ans))
