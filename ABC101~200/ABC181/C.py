import math


def dist(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def is_linear(x1, x2, x3, y1, y2, y3):
    dist_12 = dist(x1, x2, y1, y2)
    dist_13 = dist(x1, x3, y1, y3)
    dist_23 = dist(x2, x3, y2, y3)

    eps = 1e-10

    if (dist_12 - dist_13 + dist_23) < eps \
            or (dist_13 - dist_12 + dist_23) < eps \
            or (dist_23 - dist_12 + dist_13) < eps:

        return True
    else:
        return False


N = int(input())

x = []
y = []

for i in range(N):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)

is_exist = False

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and k != i:
                if is_linear(x[i], x[j], x[k], y[i], y[j], y[k]):
                    is_exist = True

if is_exist:
    print("Yes")
else:
    print("No")
