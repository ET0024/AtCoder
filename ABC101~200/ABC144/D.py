import math

a, b, x = map(int, input().split())

if x >= a * a * b / 2:
    theta = math.atan(2 * (b / a - x / (a ** 3)))
    print(theta * 180 / math.pi)
else:
    theta = math.atan(a * b * b / 2 / x)
    print(theta * 180 / math.pi)
