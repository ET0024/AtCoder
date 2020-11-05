N = int(input())

sum = 0

for i in range(N):
    a, b = map(int, input().split())
    sum += b * (b + 1) / 2 - (a - 1) * a / 2

print(int(sum))