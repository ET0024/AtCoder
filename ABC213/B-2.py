n = int(input())
a = list(map(int, input().split()))
b = [(a[i], i + 1) for i in range(n)]
print(sorted(b)[-2][1])
