a, b = map(int, input().split())

for n in range(1001):
    if (n * 8) // 100 == (a * 100) // 100 and (n * 10) // 100 == (b * 100) // 100:
        print(n)
        exit()

print(-1)