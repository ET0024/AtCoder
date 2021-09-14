N, Y = map(int, input().split())

for x in range(N + 1):  # 0...n
    for y in range(N + 1 - x):  # 0...n-i
        z = N - x - y
        gain = 10000 * x + 5000 * y + 1000 * z
        if gain == Y:
            print(x, y, z)
            exit()

print(-1, -1, -1)
