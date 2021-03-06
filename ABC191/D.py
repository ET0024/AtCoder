import math
import time

x, y, r = map(float, input().split())

x_range_max = math.floor(x + r)
x_range_min = math.ceil(x - r)

if x_range_max < x_range_min:
    print(0)
    exit()

count = 0
for i in range(x_range_min, x_range_max + 1):
    j_max = math.floor(y + math.sqrt(r ** 2 - (float(i) - x) ** 2))
    j_min = math.ceil(y - math.sqrt(r ** 2 - (float(i) - x) ** 2))

    if j_max >= j_min:
        param = 10
        j_max += param
        while (float(i) - x) ** 2 + (j_max - y) ** 2 > r ** 2:
            j_max -= 1

        j_min -= param
        while (float(i) - x) ** 2 + (j_min - y) ** 2 > r ** 2:
            j_min += 1

        count += j_max - j_min + 1

print(count)
