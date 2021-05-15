import sys

sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
indeg = [0 for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    indeg[y - 1] += 1
    graph[x - 1].append(y - 1)

start_nodes = []
for i, deg in enumerate(indeg):
    if deg == 0:
        start_nodes.append(i)


def dfs(node):
    # returns the length of longest path from given node
    # print('node:', node, 'dist:', dist[node])
    if dist[node] >= 0:
        return dist[node]
    elif len(graph[node]) == 0:
        dist[node] = 0
        return 0
    else:
        tmp = 0
        for nx in graph[node]:
            if dist[nx] >= 0:
                d = dist[nx]
            else:
                d = dfs(nx)
            dist[nx] = d
            if d > tmp:
                tmp = d

        return tmp + 1


ans = 0
dist = [-1 for _ in range(n)]
for s in start_nodes:

    tmp = dfs(s)
    if tmp > ans:
        ans = tmp

print(ans)
