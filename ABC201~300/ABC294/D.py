import heapq

N, Q = map(int, input().split())
head = 0
finished = [False for _ in range(N)]
q = []

for _ in range(Q):

    event = input()
    if event[0] == '1':
        heapq.heappush(q, head)
        head += 1
    elif event[0] == '2':
        num, x = map(int, event.split())
        finished[x - 1] = True
    else:
        while True:
            candidate = heapq.heappop(q)
            if not finished[candidate]:
                print(candidate + 1)
                heapq.heappush(q, candidate)
                break
