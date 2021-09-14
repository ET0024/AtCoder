n, h = map(int, input().split())
a = []
b = []
for _ in range(n):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)

a.sort(reverse=True)
b.sort(reverse=True)

ans = 0
for i in range(n):
    if h <= 0:
        print(ans)
        exit()
    if b[i] > a[0]:
        ans += 1
        h -= b[i]
    else:
        break

if h > 0:
    ans += 1 + (h - 1) // a[0]

print(ans)
