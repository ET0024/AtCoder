    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]

    for i, row in enumerate(a):
        for j, col in enumerate(row):
            if a[i][j] == '+':
                a[i][j] = 1
            else:
                a[i][j] = -1

    dp = [[0] * w for _ in range(h)]


    def is_takahashi(i, j):
        if (i + j) % 2 == 0:
            return True
        else:
            return False


    for i in reversed(range(h)):
        for j in reversed(range(w)):
            if i + 1 == h and j + 1 == w:
                dp[i][j] = 0
            elif i + 1 == h:
                if is_takahashi(i, j):
                    dp[i][j] = dp[i][j + 1] + a[i][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1] - a[i][j + 1]
            elif j + 1 == w:
                if is_takahashi(i, j):
                    dp[i][j] = dp[i + 1][j] + a[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] - a[i + 1][j]
            else:
                if is_takahashi(i, j):
                    dp[i][j] = max(dp[i + 1][j] + a[i + 1][j], dp[i][j + 1] + a[i][j + 1])
                else:
                    dp[i][j] = min(dp[i + 1][j] - a[i + 1][j], dp[i][j + 1] - a[i][j + 1])

    # debug
    # for r in dp:
    #     print(r)
    # print('score:', dp[0][0])

    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')
