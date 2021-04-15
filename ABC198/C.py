import math

r, x, y = map(int, input().split())

dist = math.sqrt(x ** 2 + y ** 2)

if dist == r:
    print(1)

elif dist < r:
    print(2)
else:
    print(math.ceil(dist/r))
