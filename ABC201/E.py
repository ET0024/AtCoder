import heapq

N = int(input())

g = [[] for _ in range(N)]
deg = [0 for _ in range(N)]
dist = [float('inf') for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    deg[u] += 1
    g[u].append((v, w))
    deg[v] += 1
    g[v].append((u, w))

for i in range(N):
    if deg[i] == 1:
        start = i
        break
q = []
dist[start] = 0
heapq.heappush(q, (0, start))

# 以下dijkstraでの実装
# weightのXORで距離が定義されるので、dijkstraは適切でないかもしれない
# -> negative weightと同じ影響がありそう
#    ex. 6(101) xor 5(110) = 3(011)
# 今回はTreeで各Nodeを1回しか訪れないためACしたと思われる

while len(q) > 0:
    d, node = heapq.heappop(q)
    visited[node] = True
    for node2, weight in g[node]:
        if not visited[node2] and d ^ weight < dist[node2]:
            dist[node2] = d ^ weight
            heapq.heappush(q, (d ^ weight, node2))

ans = 0
for k in range(1, 61):
    count_0 = 0
    count_1 = 0
    for d in dist:
        if d >> (k - 1) & 1 == 0:
            count_0 += 1
        else:
            count_1 += 1

    ans += count_0 * count_1 * (2 ** (k - 1))

print(ans % (10 ** 9 + 7))
