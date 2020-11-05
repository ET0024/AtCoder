def check_colliniarity(x1, y1, x2, y2, x3, y3):
    if (y2-y1)*(x3-x1) ==(y3-y1)*(x2-x1):
        return True
    else:
        return False

N = int(input())

x, y = [], []

for i in range(N):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if check_colliniarity(x[i], y[i], x[j], y[j], x[k], y[k]):
                print("Yes")
                exit()

print("No")