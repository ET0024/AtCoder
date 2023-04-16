a, b = map(int, input().split())
count = 0

while True:
    if a == b:
        break
    elif a > b:
        count += (a - 1) // b
        a = a - b * ((a - 1) // b)
    else:
        count += (b - 1) // a
        b = b - a * ((b - 1) // a)

print(count)
