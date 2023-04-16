# bit全探索の練習
h1, w1 = map(int, input().split())
a1 = []
for _ in range(h1):
    a1.append(list(map(int, input().split())))

h2, w2 = map(int, input().split())
a2 = []
for _ in range(h2):
    a2.append(list(map(int, input().split())))

# bit全探索
H_ALL = 1 << h1
W_ALL = 1 << w1

for h_pattern in range(H_ALL):
    for w_pattern in range(W_ALL):
        a_extracted = [[-1] * w2 for _ in range(h2)]
        rowno = -1
        for i in range(h1):
            colno = -1
            if h_pattern >> i & 1:
                rowno += 1
                if rowno >= h2:
                    break
                for j in range(w1):
                    if w_pattern >> j & 1:
                        colno += 1
                        if colno >= w2:
                            break
                        a_extracted[rowno][colno] = a1[i][j]
        isSame = True
        for i in range(h2):
            if a_extracted[i] != a2[i]:
                isSame = False
                break
        if isSame:
            print('Yes')
            exit()

print('No')
