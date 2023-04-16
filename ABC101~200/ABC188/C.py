n = int(input())
a = list(map(int, input().split()))
d = {}
for i, val in enumerate(a):
    d[val] = i + 1

candidate1 = max(a[:2 ** (n - 1)])
candidate2 = max(a[2 ** (n - 1):])

print(d[min(candidate1, candidate2)])
