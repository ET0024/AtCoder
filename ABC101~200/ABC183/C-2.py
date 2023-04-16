import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
l = [i for i in range(N)]
count = 0
for pat in itertools.permutations(l):
    if pat[0] != 0:
        continue
    cost = 0
    for i in range(len(pat)):
        cost += T[pat[i - 1]][pat[i]]
    if cost == K:
        count += 1

print(count)
