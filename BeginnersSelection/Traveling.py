def is_reachable(t, x, y):
    print("debug: t, x, y = ", t, x, y)

    if (t >= abs(x) + abs(y)) & ((t - abs(x) - abs(y)) % 2 == 0):
        print("debug: OK")
        return True
    else:
        print("debug: NG")
        return False


n = int(input())

isFeasible = True
t, x, y = 0, 0, 0

for i in range(n):
    previous_t = t
    previous_x = x
    previous_y = y
    t, x, y = map(int, input().split())
    isFeasible *= is_reachable(t - previous_t, x - previous_x, y - previous_y)

if isFeasible:
    print("Yes")
else:
    print("No")
