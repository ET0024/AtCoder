import bisect


# f(i):iを出来る限り平方数で割った値 となるf(0<=i<=n)を返す
def calc(n):
    f = [i for i in range(n + 1)]

    for i in range(2, n + 1):
        if i ** 2 > n:
            break

        for j in range(1, n + 1):
            if i ** 2 * j > n:
                break
            while f[i ** 2 * j] % i ** 2 == 0:
                f[i ** 2 * j] //= i ** 2
    return f


n = int(input())
f = calc(n)
square_list = [i ** 2 for i in range(1, n + 1)]

ans = 0
for i in range(1, n + 1):
    target = n // f[i]
    ans += bisect.bisect_right(square_list, target)

print(ans)
