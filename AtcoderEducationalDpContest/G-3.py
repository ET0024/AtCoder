import sys

sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
edges = [[] for _ in range(N)]
indeg = [0 for _ in range(N)]
dist = [-1 for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    edges[x - 1].append(y - 1)
    indeg[y - 1] += 1


def dfs(node):
    if dist[node] >= 0:
        return dist[node]
    if len(edges[node]) == 0:
        dist[node] = 0
        return 0
    ret = 0
    for nx in edges[node]:
        dist[nx] = dfs(nx)
        if dist[nx] > ret:
            ret = dist[nx]
    dist[node] = ret + 1
    return ret + 1


ans = 0
for i, d in enumerate(indeg):
    if d == 0:
        tmp = dfs(i)
        ans = max(ans, tmp)

print(ans)
