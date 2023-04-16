n = int(input())
a = list(map(int, input().split()))
x = int(input())
total = sum(a)

ans = (x // total) * n
x %= total
for i, val in enumerate(a):
    x -= val
    if x < 0:
        ans += (i + 1)
        break

print(ans)
