def rotate(x, size):
    x_new = [[-1] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            # x_new[i][j] = x[n - 1 - j][i]
            x_new[i][j] = x[j][n - 1 - i] #逆回転
    return x_new


n = int(input())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))

for _ in range(4):
    a = rotate(a, n)
    same = True
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] != 1:
                same = False
    if same:
        print('Yes')
        exit()

print('No')
