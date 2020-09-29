a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

for _a in range(a+1):
    for _b in range(b+1):
        for _c in range(c+1):
            if 500*_a + 100*_b + 50*_c == x:
                count += 1

print(count)

