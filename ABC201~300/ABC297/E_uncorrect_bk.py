n, k = map(int, input().split())
A = sorted(map(int, input().split()))

possible_set = set()
news = [0]

for _ in range(k + 1):
    # print('len possibleset', len(possible_set))
    candidate = set()
    for new in news:
        for a in A:
            candidate.add(new + a)
    news = candidate.difference(possible_set)
    # print('len news', len(news))
    possible_set = possible_set.union(news)
    if len(possible_set) > k:
        break

print(sorted(list(possible_set))[k - 1])
