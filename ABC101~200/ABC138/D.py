from collections import deque

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

added = [0 for _ in range(N)]
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    added[p] += x

counter = [-1 for _ in range(N)]
counter[0] = added[0]
q = deque()
q.append(0)
while len(q) > 0:
    current = q.popleft()

    for nx in edge[current]:
        if counter[nx] < 0:
            counter[nx] = counter[current] + added[nx]
            q.append(nx)

print(*counter)
