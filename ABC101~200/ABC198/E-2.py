import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
c = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

visited = [False] * n
good = [False] * n
color = [0] * (10 ** 5 + 1)


def dfs(node):
    visited[node] = True

    if color[c[node]] == 0:
        good[node] = True

    color[c[node]] += 1

    for nx in g[node]:
        if not visited[nx]:
            dfs(nx)

    color[c[node]] -= 1


dfs(0)
for index, g in enumerate(good):
    if g:
        print(index + 1)
