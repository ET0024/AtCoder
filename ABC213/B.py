n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n):
    b.append((a[i], i + 1))

print(sorted(b)[-2][1])
