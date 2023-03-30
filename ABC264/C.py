import itertools

h1, w1 = map(int, input().split())
a1 = []
for _ in range(h1):
    a1.append(list(map(int, input().split())))

h2, w2 = map(int, input().split())
a2 = []
for _ in range(h2):
    a2.append(list(map(int, input().split())))

rows = list(range(h1))
cols = list(range(w1))

for row in itertools.combinations(rows, h2):
    for col in itertools.combinations(cols, w2):
        result = [[-1] * w2 for _ in range(h2)]
        for i, rowno in enumerate(list(row)):
            for j, colno in enumerate(list(col)):
                result[i][j] = a1[rowno][colno]

        isSame = True
        for i in range(h2):
            if result[i] != a2[i]:
                isSame = False

        if isSame:
            print('Yes')
            exit()

print('No')
