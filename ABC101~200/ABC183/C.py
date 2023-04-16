import itertools

N, K = map(int, input().split())

T = []
for _ in range(N):
    T.append(list(map(int, input().split())))

nodes = list(range(1, N))

ans = 0
for pair in itertools.permutations(nodes):
    pair = [0] + list(pair)
    travel_time = 0

    for i in range(N):
        travel_time += T[pair[i]][pair[i - 1]]

    if travel_time == K:
        ans += 1

print(ans)
