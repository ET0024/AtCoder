import heapq

Q = int(input())
q = []

plus = 0

for _ in range(Q):
    tmp = input()
    query = tmp[0]

    if query == '1':
        _, x = tmp.split()
        x = int(x)
        heapq.heappush(q, x - plus)
    elif query == '2':
        _, x = tmp.split()
        x = int(x)
        plus += x
    else:
        print(heapq.heappop(q) + plus)
