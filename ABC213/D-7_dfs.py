import sys

sys.setrecursionlimit(10 ** 9)

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)


def dfs(current):
    ans.append(current + 1)
    if visited[current]:
        return
    visited[current] = True
    nxs = sorted(edge[current])
    for nx in nxs:
        if not visited[nx]:
            dfs(nx)
            ans.append(current + 1)


visited = [False for _ in range(n)]
ans = []
dfs(0)

print(*ans)
