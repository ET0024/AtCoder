N, X = map(int, input().split())

current = 0

for i in range(N):
    v, p = map(int, input().split())
    current += v * p
    if current > X * 100:
        print(i + 1)
        exit()

print(-1)
