import itertools

h1, w1 = map(int, input().split())
a1 = []
for _ in range(h1):
    a1.append(list(map(int, input().split())))

h2, w2 = map(int, input().split())
a2 = []
for _ in range(h2):
    a2.append(list(map(int, input().split())))

for h_pattern in itertools.combinations(list(range(h1)), h2):
    for w_pattern in itertools.combinations(list(range(w1)), w2):
        a3 = [[-1] * w2 for _ in range(h2)]
        for h_to, h_from in enumerate(h_pattern):
            for w_to, w_from in enumerate(w_pattern):
                a3[h_to][w_to] = a1[h_from][w_from]

        if a3 == a2:
            print('Yes')
            exit()

print('No')
