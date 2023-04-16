n = int(input())
a = list(map(int, input().split()))

minus_count = 0
for val in a:
    if val < 0:
        minus_count += 1

b = list(map(lambda x: abs(x), a))
b.sort()

if minus_count % 2 == 0:
    print(sum(b))
else:
    b[0] = -b[0]
    print(sum(b))
