n = int(input())
x = list(map(int, input().split()))

xs = sorted(x)
mid1 = xs[n // 2 - 1]
mid2 = xs[n // 2]

for i in range(n):
    if x[i] <= mid1:
        print(mid2)
    else:
        print(mid1)
