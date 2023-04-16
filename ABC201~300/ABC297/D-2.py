a, b = map(int, input().split())

count = 0
while True:
    if a > b:
        count += (a - 1) // b
        a -= b * ((a - 1) // b)
    elif a < b:
        count += (b - 1) // a
        b -= a * ((b - 1) // a)
    else:
        break

print(count)