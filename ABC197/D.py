from math import cos
from math import sin
from math import pi

n = int(input())

x, y = map(int, input().split())
x_op, y_op = map(int, input().split())

x_c, y_c = (x + x_op) / 2, (y + y_op) / 2

theta = 2 * pi / n
x1 = x_c + (x - x_c) * cos(theta) - (y - y_c) * sin(theta)
y1 = y_c + (x - x_c) * sin(theta) + (y - y_c) * cos(theta)

print(x1, y1)
