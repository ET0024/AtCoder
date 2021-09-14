def f(a, b):
    da = 0
    db = 0
    while a > 0:
        a //= 10
        da += 1

    while b > 0:
        b //= 10
        db += 1

    return max(da, db)


n = int(input())

ans = float('inf')
for i in range(1, n + 1):
    if i ** 2 > n:
        break

    if n % i == 0:
        j = n // i
        tmp = f(i, j)
        if tmp < ans:
            ans = tmp

print(ans)
