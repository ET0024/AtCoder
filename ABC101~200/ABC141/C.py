n, k, q = map(int, input().split())

scored = [0 for _ in range(n)]
for _ in range(q):
    scored[int(input()) - 1] += 1

for i in range(n):
    if k - q + scored[i] > 0:
        print('Yes')
    else:
        print('No')
