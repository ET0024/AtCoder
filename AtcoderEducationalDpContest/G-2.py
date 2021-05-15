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
    elif len(edges[node]) == 0:
        dist[node] = 0
        return 0
    else:
        ret = 0
        for nx in edges[node]:
            dist[nx] = dfs(nx)
            ret = max(ret, dist[nx] + 1)
        return ret


ans = 0
for i, deg in enumerate(indeg):
    if deg == 0:
        ans = max(ans, dfs(i))
print(ans)
