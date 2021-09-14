n = int(input())
x = []
y = []
for _ in range(n):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if (y[j] - y[i]) * (x[k] - x[i]) == (y[k] - y[i]) * (x[j] - x[i]):
                print('Yes')
                exit()

print('No')
