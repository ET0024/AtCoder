import sys

sys.setrecursionlimit(1000000)
from collections import deque

n = int(input())
c = list(map(int, input().split()))

g = [[] for _ in range(n)]
visited = [False] * n
good = [False] * n

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

color = [0 for _ in range(10 ** 5 + 1)]


def dfs(node):
    visited[node] = True

    if color[c[node]] == 0:
        good[node] = True

    color[c[node]] += 1

    for nxt in g[node]:
        if visited[nxt]:
            continue

        dfs(nxt)
    color[c[node]] -= 1


dfs(0)
for i, g in enumerate(good):
    if g:
        print(i + 1)
