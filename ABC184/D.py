A, B, C = map(int, input().split())
N = 101

f = [[[0] * N for i in range(N)] for i in range(N)]

f[99][99][99] = 1

for i in range(N - 2, -1, -1):
    for j in range(N - 2, -1, -1):
        for k in range(N - 2, -1, -1):
            if i * j * k == 99 ** 3 or i + j + k == 0:
                break

            tmp = 0
            if i < 99:
                tmp += (1 + f[i + 1][j][k]) * i / (i + j + k)
            else:
                tmp += 1 * i / (i + j + k)
            if j < 99:
                tmp += (1 + f[i][j + 1][k]) * j / (i + j + k)
            else:
                tmp += 1 * j / (i + j + k)
            if k < 99:
                tmp += (1 + f[i][j][k + 1]) * k / (i + j + k)
            else:
                tmp += 1 * k / (i + j + k)

            f[i][j][k] = tmp

print(f[A][B][C])
exit()
