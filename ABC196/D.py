is_debug_mode = False

def debug(*args):
    global is_debug_mode
    if is_debug_mode:
        print(*args)


def search(i, j, a, b):
    global used
    global res
    debug('###currently at:', i, j, a, b)
    debug('---used status---')
    for row in used:
        debug(row)

    if a < 0 or b < 0:
        debug('returned with 0')
        return 0
    if j == w:
        i += 1
        j = 0
        debug('(i, j) replaced to (', i, j, ')')
    if i == h:
        res += 1
        debug('end with 1:', i, j)
        return 0
    if used[i][j]:
        debug('already used:', j, j)
        search(i, j + 1, a, b)
        return 0

    # place 1*1
    used[i][j] = True
    debug('now placed b on (', i, j, ')')
    for row in used:
        debug(row)

    search(i, j + 1, a, b - 1)
    used[i][j] = False

    # place 1*2 horizontally
    if j + 1 < w and not used[i][j + 1] and a > 0:
        debug('place a　horizontally on (', i, j, ')')
        used[i][j] = True
        used[i][j + 1] = True
        search(i, j + 2, a - 1, b)
        used[i][j] = False
        used[i][j + 1] = False

    # place 1*2 vertically
    if i + 1 < h and not used[i + 1][j] and a > 0:
        debug('place a vertically on (', i, j, ')')
        used[i][j] = True
        used[i + 1][j] = True
        search(i, j + 1, a - 1, b)
        used[i][j] = False
        used[i + 1][j] = False


h, w, a, b = map(int, input().split())
res = 0

# 備忘：usedの誤った定義。各rowが同じ参照になってしまう,,
# used = [[False] * w] * h

used = [[False] * w for _ in range(h)]
search(0, 0, a, b)
print(res)
