from collections import deque

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

q = deque()
q.append(0)
ans = []
visited = [False for _ in range(n)]
while len(q) > 0:
    # print(list(map(lambda x: x+1, q)))
    node = q.pop()

    if visited[node]:
        ans.append(node + 1)
        continue

    ans.append(node + 1)
    visited[node] = True
    nxs = edge[node]
    nxs.sort(reverse=True)
    for nx in nxs:
        if not visited[nx]:
            q.append(node)
            q.append(nx)
            # visited[nx] = True

print(*ans)
