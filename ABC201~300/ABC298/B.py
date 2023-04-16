n = int(input())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

prev = [[-1] * n for _ in range(n)]

for _ in range(4):
    for i in range(n):
        for j in range(n):
            prev[i][j] = a[i][j]

    for i in range(n):
        for j in range(n):
            a[i][j] = prev[n - 1 - j][i]

    ans = True
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] != 1:
                ans = False
    if ans:
        print('Yes')
        exit()

print('No')
