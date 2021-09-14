import copy

H, W, K = map(int, input().split())
c = [list(input()) for _ in range(H)]

H_ALL = 1 << H
W_ALL = 1 << W

ans = 0
for h_pattern in range(H_ALL):
    for w_pattern in range(W_ALL):
        c_copy = copy.deepcopy(c)
        for h in range(H):
            if h_pattern >> h & 1:
                # cのh行目を塗りつぶす
                for j in range(W):
                    c_copy[h][j] = 'r'
        for w in range(W):
            if w_pattern >> w & 1:
                for i in range(H):
                    c_copy[i][w] = 'r'
        count = 0
        for row in c_copy:
            count += row.count('#')

        if count == K:
            ans += 1

print(ans)