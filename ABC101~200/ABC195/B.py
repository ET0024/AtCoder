import math
a, b, w = map(int, input().split())

w *= 1000
found = False
min = 1E10
max = -1

for i in range(math.floor(w / b), math.ceil(w / a) + 1):
    if a * i <= w <= b * i:
        found = True
        if i < min:
            min = i
        if max < i:
            max = i

if not found:
    print('UNSATISFIABLE')
else:
    print(min, max)
