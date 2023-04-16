import heapq

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
r_edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c))
    r_edge[b].append((a, c))

for k in range(N):

    k_edge = edge[:k+1]
    k_r_edge = r_edge[:k+1]
    print(k, k_edge)
