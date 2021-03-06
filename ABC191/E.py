import heapq


def dijkstra(graph, start):
    dist = [float("inf")] * (n + 1)
    searched = [False] * (n + 1)
    hq = []
    hq.append([0, start])

    while len(hq):
        d, current = heapq.heappop(hq)

        if not searched[current]:
            searched[current] = True
            for to, cost in graph[current]:
                if dist[to] > d + cost:
                    dist[to] = d + cost
                    heapq.heappush(hq, [dist[to], to])

    return dist


# グラフ（隣接リスト）構築
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

# 探索・結果表示
for i in range(1, n + 1):
    dist = dijkstra(graph, i)[i]

    if dist == float("inf"):
        print(-1)
    else:
        print(dist)
