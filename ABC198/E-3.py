import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
c = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

visited = [False] * n
good = [False] * n
color = [0] * (10 ** 5 + 1)


def dfs(node):
    visited[node] = True
    color[c[node]] += 1
    if color[c[node]] <= 1:
        good[node] = True

    for nx in g[node]:
        if not visited[nx]:
            dfs(nx)
    color[c[node]] -= 1


dfs(0)
for i, g in enumerate(good):
    if g:
        print(i + 1)
