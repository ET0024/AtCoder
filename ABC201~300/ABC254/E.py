from collections import deque
from collections import defaultdict

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())
    ans = 0
    x -= 1
    q = deque()
    # dist = [-1 for _ in range(n)]
    dist = defaultdict(lambda: -1)
    # searched = [False for _ in range(n)]
    searched = defaultdict(lambda: False)
    dist[x] = 0
    q.append((0, x))
    ans += x + 1
    while len(q) > 0:
        cost, current = q.popleft()
        if cost + 1 > k:
            break
        if searched[current]:
            continue

        for nx in edge[current]:
            if dist[nx] < 0:
                dist[nx] = cost + 1
                q.append((cost + 1, nx))
                ans += nx + 1
        searched[current] = True

    print(ans)
