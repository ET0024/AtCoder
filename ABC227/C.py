n = int(input())
ans = 0
for a in range(1, n+1):
    if a ** 3 > n:
        break
    res = n // a
    for b in range(a, res + 1):
        if b ** 2 > res:
            break

        ans += max(0, res // b - b + 1)

print(ans)
