N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)


def dfs(i, color):
    if i == N:
        return 1
    next_color = set()
    for nx in edge[i]:
        next_color.add(color[nx])
    not_used_color = set([1, 2, 3]) - next_color

    ans = 0
    for nuc in not_used_color:
        color[i] = nuc
        ans += dfs(i + 1, color)

    return ans


print(dfs(0, [-1 for _ in range(N)]))
