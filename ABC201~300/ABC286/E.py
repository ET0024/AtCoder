import heapq

n = int(input())
souvenir = list(map(int, input().split()))
route = []
for _ in range(n):
    route.append(list(input()))

iter_num = int(input())
cost = [[(-1, -1)] * n for _ in range(n)]
calculated = [False] * n
for _ in range(iter_num):
    u, v = map(int, input().split())
    start = u - 1
    end = v - 1

    if calculated[start]:
        dist, val = cost[start][end]
        if dist == -1:
            print('Impossible')
        else:
            print(dist, -val)
        continue

    q = []
    visited = [False] * n

    heapq.heappush(q, ((0, -souvenir[start]), start))

    while len(q) > 0:
        (dist, val), current = heapq.heappop(q)
        if visited[current]:
            continue
        visited[current] = True
        cost[start][current] = (dist, val)

        for nxt in range(n):
            if route[current][nxt] == 'N' or visited[nxt]:
                continue
            heapq.heappush(q, ((dist + 1, val - souvenir[nxt]), nxt))
    calculated[start] = True

    dist, val = cost[start][end]
    if dist == -1:
        print('Impossible')
    else:
        print(dist, -val)

