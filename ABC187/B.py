N = int(input())
x, y = [], []

for _ in range(N):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)

count = 0

for i in range(N - 1):
    for j in range(i + 1, N):

        z = (y[j] - y[i]) / (x[j] - x[i])

        if -1 <= z <= 1:
            count += 1

print(count)
