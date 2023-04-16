n = int(input())
x, y, p = [], [], []
for _ in range(n):
    _x, _y, _p = map(int, input().split())
    x.append(_x)
    y.append(_y)
    p.append(_p)

INF = 10 ** 10

# 二分探索
ok = INF
ng = 0
while ok - ng > 1:
    mid = (ok + ng) // 2

    # x = midに対するWF
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mid * p[i] >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                dist[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] == 0:
                    dist[i][j] = 0
    is_ok = False
    for start in range(n):
        if max(dist[start]) == 0:
            is_ok = True
    if is_ok:
        ok = mid
    else:
        ng = mid

print(ok)
