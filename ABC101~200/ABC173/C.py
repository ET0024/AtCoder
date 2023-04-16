import copy

H, W, K = map(int, input().split())
c = [list(input()) for _ in range(H)]

ROW_ALL = 1 << H
COL_ALL = 1 << W

count = 0
for row in range(ROW_ALL):
    for col in range(COL_ALL):
        c_copy = copy.deepcopy(c)

        for h in range(H):
            if (row >> h) & 1 == 1:
                for i in range(W):
                    c_copy[h][i] = 'r'
                # print(h, '行目の塗りつぶし')
        for w in range(W):
            if (col >> w) & 1 == 1:
                for j in range(H):
                    c_copy[j][w] = 'r'
                # print(w, '列目の塗りつぶし')

        ans = 0

        for i in range(H):
            ans += c_copy[i].count('#')

        if ans == K:
            count += 1
        # for r in c_copy:
        #     print(r)
        # print('------------------------------')
print(count)
