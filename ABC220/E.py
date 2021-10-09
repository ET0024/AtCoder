from collections import defaultdict

N = 7
n = 2 ** N - 1
edge = [[] for _ in range(n)]
dist = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0
for i in range(1, 2 ** (N - 1)):
    edge[i - 1].append(2 * i - 1)
    edge[i - 1].append(2 * i)
    edge[2 * i - 1].append(i - 1)
    edge[2 * i].append(i - 1)
    dist[i - 1][2 * i - 1] = 1
    dist[i - 1][2 * i] = 1
    dist[2 * i - 1][i - 1] = 1
    dist[2 * i][i - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

d = defaultdict(int)
for i in range(n):
    for j in range(n):
        d[dist[i][j]] += 1

print(d)
