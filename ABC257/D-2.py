n = int(input())
x, y, p = [], [], []
for _ in range(n):
    _x, _y, _p = map(int, input().split())
    x.append(_x)
    y.append(_y)
    p.append(_p)

INF = 10 ** 10
ng = 0
ok = INF

while ok - ng > 1:
    mid = (ok + ng) // 2

    # midに対する判定
    # distの初期化
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mid * p[i] >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                dist[i][j] = 0

    # WF法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] == 0:
                    dist[i][j] = 0
    # 判定
    isok = False
    for i in range(n):
        if max(dist[i]) == 0:
            isok = True

    if isok:
        ok = mid
    else:
        ng = mid

print(ok)
