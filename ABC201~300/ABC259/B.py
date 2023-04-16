import math
a, b, d = map(int, input().split())
cos = math.cos(math.pi*d/180)
sin = math.sin(math.pi*d/180)
x = cos * a - sin * b
y = sin * a + cos * b
print(x, y)