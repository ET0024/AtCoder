from collections import deque

N = int(input())
P = list(map(int, input().split()))
edge = [[] for _ in range(N)]

for i, p in enumerate(P):
    edge[i + 1].append(p - 1)
    edge[p - 1].append(i + 1)

dist = [-1 for _ in range(N)]
in_time = [-1 for _ in range(N)]
out_time = [-1 for _ in range(N)]
visited = [False for _ in range(N)]

q = deque()
dist[0] = 0
q.append(0)
count = 0

while len(q) > 0:
    count += 1
    node = q.pop()
    if not visited[node]:
        in_time[node] = count
        q.append(node)
        visited[node] = True
    else:
        out_time[node] = count

    for nx in edge[node]:
        if not visited[nx]:
            dist[nx] = dist[node] + 1
            q.append(nx)

print(visited)
print(dist)
print(in_time)
print(out_time)