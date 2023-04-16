import heapq

Q = int(input())
q = []
res = 0
for _ in range(Q):
    query = input()
    if query[0] == '3':
        print(heapq.heappop(q) + res)
    elif query[0] == '2':
        _, x = map(int, query.split())
        res += x
    elif query[0] == '1':
        _, x = map(int, query.split())
        heapq.heappush(q, x - res)
