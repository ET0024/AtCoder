from collections import deque

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

ans = [-1 for _ in range(n)]
visited = [False for _ in range(n)]

q = deque()
q.append(0)
visited[0] = True
while len(q) > 0:
    current = q.popleft()
    for nx in edge[current]:
        if not visited[nx]:
            ans[nx] = current
            q.append(nx)
            visited[nx] = True

print('Yes')
for i in range(1, n):
    print(ans[i] + 1)
