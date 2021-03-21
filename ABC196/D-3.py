def dfs(i, j):
    global used, count, a, b

    if a < 0 or b < 0:
        return
    if j == w:
        i += 1
        j = 0
    if i == h:
        count += 1
        return
    # check if used
    if used[i][j]:
        dfs(i, j + 1)
        return

    # place 1*1
    used[i][j] = True
    b -= 1
    dfs(i, j + 1)
    used[i][j] = False
    b += 1

    # place 1*2 horizontally
    if j + 1 < w and not used[i][j + 1]:
        used[i][j] = True
        used[i][j + 1] = True
        a -= 1
        dfs(i, j + 1)
        used[i][j] = False
        used[i][j + 1] = False
        a += 1
    if i + 1 < h and not used[i + 1][j]:
        used[i][j] = True
        used[i + 1][j] = True
        a -= 1
        dfs(i, j + 1)
        used[i][j] = False
        used[i + 1][j] = False
        a += 1


h, w, a, b = map(int, input().split())
used = [[False] * w for _ in range(h)]
count = 0
dfs(0, 0)
print(count)
