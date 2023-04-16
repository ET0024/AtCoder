n, k, q = map(int, input().split())
a = list(map(int, input().split()))
L = list(map(int, input().split()))

a.append(n + 1)
for l in L:
    if a[l - 1] + 1 < a[l]:
        a[l - 1] += 1
print(*a[:-1])
