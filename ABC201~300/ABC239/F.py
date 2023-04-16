import heapq

n, m = map(int, input().split())
d = list(map(int, input().split()))

# connected = []
# not_connected = [(-x, i) for i, x in enumerate(d)]
# heapq.heapify(not_connected)

connected = [False for _ in range(n)]
degree = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    connected[a] = True
    connected[b] = True
    degree[a] += 1
    degree[b] += 1

connected_pair = []
unconnected_pair = []
for node in range(n):
    if connected[node]:
        heapq.heappush(connected_pair, (degree[node] - d[node], node))
    else:
        heapq.heappush(unconnected_pair, (degree[node] - d[node], node))

ans = []
for _ in range(n - m - 1):
    # print('debug:', len(connected_pair))
    # print('debug:', len(unconnected_pair))
    # print('---')
    if len(unconnected_pair) > 0:
        if len(connected_pair) == 0:
            c_score, c_node = heapq.heappop(unconnected_pair)
            uc_score, uc_node = heapq.heappop(unconnected_pair)
            heapq.heappush(connected_pair, (c_score + 1, c_node))
            heapq.heappush(connected_pair, (uc_score + 1, uc_node))
            ans.append((c_node + 1, uc_node + 1))
        else:
            c_score, c_node = heapq.heappop(connected_pair)
            uc_score, uc_node = heapq.heappop(unconnected_pair)
            heapq.heappush(connected_pair, (c_score + 1, c_node))
            heapq.heappush(connected_pair, (uc_score + 1, uc_node))
            ans.append((c_node + 1, uc_node + 1))
    else:
        c_score, c_node = heapq.heappop(connected_pair)
        uc_score, uc_node = heapq.heappop(connected_pair)
        heapq.heappush(connected_pair, (c_score + 1, c_node))
        heapq.heappush(connected_pair, (uc_score + 1, uc_node))
        ans.append((c_node + 1, uc_node + 1))

if len(unconnected_pair) > 0:
    print(-1)
    exit()

for val, node in connected_pair:
    if val != 0:
        print(-1)
        exit()

for pair in ans:
    print(*pair)
