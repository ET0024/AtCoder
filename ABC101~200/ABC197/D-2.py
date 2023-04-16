import math

n = int(input())
x0, y0 = map(int, input().split())
xop, yop = map(int, input().split())

xc = (x0 + xop) / 2
yc = (y0 + yop) / 2

theta = 2 * math.pi / n

x1 = xc + (math.cos(theta) * (x0 - xc) - math.sin(theta) * (y0 - yc))
y1 = yc + (math.sin(theta) * (x0 - xc) + math.cos(theta) * (y0 - yc))

print(x1, y1)
