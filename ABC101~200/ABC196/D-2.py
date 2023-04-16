def dfs(i, j, a, b):
    global count
    global used

    if a < 0 or b < 0:
        return
    if j == w:
        i += 1
        j = 0
    if i == h:
        count += 1
        return

    if used[i][j]:
        dfs(i, j + 1, a, b)
        return

    # place 1*1 block
    used[i][j] = True
    dfs(i, j + 1, a, b - 1)
    used[i][j] = False

    # place 1*2 block horizontically
    if j + 1 < w and not used[i][j + 1]:
        used[i][j] = True
        used[i][j + 1] = True
        dfs(i, j + 1, a - 1, b)
        used[i][j] = False
        used[i][j + 1] = False

    # place 1*2 block vertically
    if i + 1 < h and not used[i + 1][j]:
        used[i][j] = True
        used[i + 1][j] = True
        dfs(i, j + 1, a - 1, b)
        used[i][j] = False
        used[i + 1][j] = False


h, w, a, b = map(int, input().split())
count = 0
used = [[False] * w for _ in range(h)]
dfs(0, 0, a, b)
print(count)
