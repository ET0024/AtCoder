import heapq


def dijkstra(graph, start):
    dist = [float('inf') for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    hq = [[0, start]]

    while len(hq) > 0:
        current_cost, current_node = heapq.heappop(hq)

        if not visited[current_node]:
            visited[current_node] = True
            for to, cost in graph[current_node]:
                if dist[to] > current_cost + cost:
                    dist[to] = current_cost + cost
                heapq.heappush(hq, [dist[to], to])

    return dist


# グラフ構築
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

# 探索
for i in range(1, n + 1):
    dist = dijkstra(graph, i)
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])
