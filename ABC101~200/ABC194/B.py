n = int(input())
a = []
b = []
for _ in range(n):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)

ans = float("inf")
for i in range(n):
    for j in range(n):

        if i == j and a[i] + b[j] < ans:
            ans = a[i] + b[j]
        elif i != j and max(a[i], b[j]) < ans:
            ans = max(a[i], b[j])
print(ans)
