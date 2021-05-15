import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
dist = [-1 for _ in range(N)]
indeg = [0 for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    edge[x - 1].append(y - 1)
    indeg[y - 1] += 1


def dfs(node):
    if dist[node] >= 0:
        return dist[node]
    if len(edge[node]) == 0:
        return 0

    ret = 0
    for nx in edge[node]:
        dist[nx] = dfs(nx)
        ret = max(ret, dist[nx])

    dist[node] = ret + 1
    return dist[node]


for i, deg in enumerate(indeg):
    if deg == 0:
        dfs(i)

print(max(dist))
