import math
import time

# def to_nth(x, n):
#     x = str(x)
#     ans = 0
#     for i in range(len(x)):
#         ans += int(x[i]) * (n ** (len(x) - i - 1))
#
#     return ans


def is_safe(x, n, m):
    x = str(x)
    residual = m
    for i in range(len(x)):
        residual -= int(x[len(x) - i - 1]) * (n ** i)

        if residual < 0:
            return False
    return True


x = int(input())
m = int(input())
x_len = len(str(x))
n_min = int(sorted(str(x))[-1]) + 1

if x_len == 1:
    if x > m:
        print(0)
        exit()
    else:
        print(1)
        exit()

# n_max = math.ceil(math.exp(math.log(m) / (x_len - 1)))
n_max = m

count = 0

l = n_min
r = n_max + 1

if not is_safe(x, n_min, m):
    print(0)
    exit()

#debug initial condition
if is_safe(x, r, m):
    time.sleep(3)
    print(-1)
    exit()


while r - l > 1:
    mid = (l + r) // 2
    if is_safe(x, mid, m):
        l = mid
    else:
        r = mid

print(l - n_min + 1)
