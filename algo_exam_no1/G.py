N = int(input())
a = [[0] * N for _ in range(N)]

for i in range(N - 1):
    row = map(int, input().split())
    for j, val in enumerate(row):
        a[i][i + 1 + j] = val
        a[i + 1 + j][i] = val

ans = - 10 ** 12

for group1 in range(1 << N):
    for group2 in range(1 << N):
        if group1 & group2 > 0:
            continue
        else:
            group3 = (1 << N) - 1 - (group1 | group2)

            happy = 0
            for i in range(N - 1):
                for j in range(i + 1, N):

                    # if (i, j) belong to same group then
                    if (group1 >> i & 1) and (group1 >> j & 1) \
                            or (group2 >> i & 1) and (group2 >> j & 1) \
                            or (group3 >> i & 1) and (group3 >> j & 1):
                        happy += a[i][j]

            if happy > ans:
                ans = happy

print(ans)
