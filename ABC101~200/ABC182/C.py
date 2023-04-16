from collections import Counter

N = list(map(int, list(input())))
N = list(map(lambda x: x % 3, N))
L = len(N)
C = Counter(N)
residual = sum(N) % 3

if residual == 0:
    print(0)
    exit()
elif residual == 1:
    if L > 1 and C[1] >= 1:
        print(1)
        exit()
    elif L > 2 and C[2] >= 2:
        print(2)
        exit()
elif residual == 2:
    if L > 1 and C[2] >= 1:
        print(1)
        exit()
    elif L > 2 and C[1] >= 2:
        print(2)
        exit()

print(-1)
