import heapq
from collections import deque

Q = int(input())

main_list = []
res_list = deque()
for _ in range(Q):
    tmp = input()
    query = tmp[0]
    if query == '1':
        x = int(tmp.split()[1])
        res_list.append(x)
    elif query == '2':
        if len(main_list) > 0:
            print(heapq.heappop(main_list))
        elif len(res_list) > 0:
            print(res_list.popleft())
    elif query == '3':
        for item in res_list:
            heapq.heappush(main_list, item)
        res_list = deque()
